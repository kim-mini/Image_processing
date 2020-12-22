txt = open('/home/mini/study/Yolo_mark/x64/Release/data/train.txt','r')
f = open('/home/mini/study/Yolo_mark/x64/Release/data/train2.txt','w')
while True :
    line = txt.readline()
    if not line:
        break
    f.write('/home/mini/study/Yolo_mark/'+line)
        
txt.close()
f.close()


# -------------------------------------------------------------------------------------------------


import os


txt = '/home/mini/study/Yolo_mark/x64/Release/data/img'
filedir = os.listdir(txt)
f = open('/home/mini/study/Yolo_mark/x64/Release/data/train.txt', 'w')

for file in filedir:
    if file.endswith('.jpg'):
        writepath = os.path.join(txt,file)
        print(writepath)
        f.write(writepath+'\n')

f.close()


# ---------------------------------------------------------------------------------------------------

# 텍스트 파일 내용 변경
# 클래스넘버가 바뀌어서 수정해주는 코드
import os


path = '/home/ubuntu/Downloads/test'
dscpath = '/home/ubuntu/Downloads/img2'
# 해당하는 클래스 넘버를 넣어준다
# 여기서는 toothbrush로 바꾸기 위함이여서 7번으로 넣어준다
classnum = '7'

FileList = os.listdir(path)

for file in FileList:
    if file.endswith('.txt'):
        # 바뀐 경로에 이름은 똑같이 저장
        srcfile = os.path.join(path,file)
        dscfile = os.path.join(dscpath,file)

        txt = open(srcfile, 'r')
        f = open(dscfile,'w')

        line = txt.readline()[1:]
        f.write(classnum+line)
        txt.close()
        f.close()
