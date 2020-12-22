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

        
---------------------------------------------------------------------------------------------------------------
# 텍스트파일과 이미지파일 둘다 바꿀때
        
import os

cnt = 60
path = '/home/ubuntu/Downloads/test'
fileList = os.listdir(path)
ext1 = '.jpg'
ext2 = '.txt'
ClassName = 'toothbrush'

txtlist = []
jpglist = []
for filename in fileList:
    #print(filename)
    file = filename.split('.')[1]
    if file == 'jpg':
        jpglist.append(filename)
    else:
        txtlist.append(filename)


for i in range(len(jpglist)):
    cnt += 1
    for j in range(len(txtlist)):
        if jpglist[i].split('.')[0] == txtlist[j].split('.')[0]:

            for srcname in fileList:
                if jpglist[i] == srcname:
                    print('a',cnt)
                    #print(jpglist[i], srcname)
                    srcpath = os.path.join(path, srcname)
                    if cnt < 10:
                        dstname = ClassName+'_00{}'.format(cnt)+ext1
                    elif cnt < 100:
                        dstname = ClassName+'_0{}'.format(cnt)+ext1
                    elif cnt < 1000:
                        dstname = ClassName + '_{}'.format(cnt) + ext1

                    dstpath = os.path.join(path, dstname)

                    os.rename(srcpath, dstpath)

                if txtlist[j] == srcname:
                    print('b',cnt)
                    # print(srcname, txtlist[j])
                    srcpath = os.path.join(path, srcname)
                    if cnt < 10:
                        dstname = ClassName + '_00{}'.format(cnt) + ext2
                    elif cnt < 100:
                        dstname = ClassName + '_0{}'.format(cnt) + ext2
                    elif cnt < 1000:
                        dstname = ClassName + '_{}'.format(cnt) + ext2

                    dstpath = os.path.join(path, dstname)


                    os.rename(srcpath, dstpath)

