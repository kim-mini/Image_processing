import os
import cv2

listTmp =os.listdir( "/home/ubuntu/Downloads/img" )
basepath = "/home/ubuntu/Downloads/img"

for filename in listTmp:
    imgpath = basepath + "/" + filename

    img = cv2.imread(imgpath, cv2.IMREAD_COLOR )

    dst = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)

    cv2.imwrite( imgpath, dst )
