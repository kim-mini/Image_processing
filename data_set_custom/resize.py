import os
import cv2

# 원본파일이 있는 경로
path = "/home/ubuntu/Downloads/data/one"
listTmp =os.listdir(path)
# 저장할 경로
Savepath = "/home/ubuntu/Downloads/convert"

for filename in listTmp:
    imgpath = path + "/" + filename

    img = cv2.imread(imgpath, cv2.IMREAD_COLOR )

    dst = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    Savefile= os.path.join(Savepath,filename)
    cv2.imwrite( Savefile, dst )
