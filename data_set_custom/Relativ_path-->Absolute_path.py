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
