import os

cnt = 1
path = '/home/mini/study/Yolo_mark/x64/Release/data/img4'
fileList = os.listdir(path)
ext = '.jpg'
ClassName = 'ramen'


for filename in fileList:
    if filename == 'Untitled.ipynb':
        break


    if filename.endswith(ext):

        srcpath = os.path.join(path, filename)
        if cnt < 10:
            dstname = ClassName+'_00{}'.format(cnt)+ext
        elif cnt < 100:
            dstname = ClassName+'_0{}'.format(cnt)+ext
        elif cnt < 1000:
            dstname = ClassName + '_{}'.format(cnt) + ext

        dstpath = os.path.join(path, dstname)


        os.rename(srcpath, dstpath)
        cnt += 1
