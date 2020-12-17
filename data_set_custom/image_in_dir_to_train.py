import os

txt = '/home/mini/study/Yolo_mark/x64/Release/data/img4'
filedir = os.listdir(txt)
f = open('/home/mini/study/Yolo_mark/x64/Release/data/train.txt', 'w')

for file in filedir:
    if file.endswith('.jpg'):
        writepath = os.path.join(txt,file)
        print(writepath)
        f.write(writepath+'\n')

f.close()
