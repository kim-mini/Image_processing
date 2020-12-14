import os
import cv2
import shutil
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random


# image path
path = '/home/mini/study/Image_processing/opencv_python/data/lena.jpg'
# save
savepath = '/home/mini/study/Image_processing/opencv_python/data/dataaugment'


if os.path.isfile(path):
    img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if os.path.exists(savepath):
        shutil.rmtree(savepath)

    os.mkdir(savepath)
else:
    print('not found \'{}\''.format(path))


class DataAugmentation():
    def __init__(self):
        self.name = 'Img'

    def RotationImage(self,img):
        RotationImg = []

        height, width, channel = img.shape

        for i in range(0,360,15):
            # print(i)
            matrix = cv2.getRotationMatrix2D((width/2, height/2), i, 1)
            RotationImg.append(matrix)

        cnt = 0
        # save to chage image
        for j in range(len(RotationImg)):
            # rotation filename
            filename = os.path.join(savepath, '{}_R_{}.jpg'.format(self.name,cnt))
            dst = cv2.warpAffine(img, RotationImg[j], (width, height))
            cv2.imwrite(filename,dst)
            cnt += 1
        print('R')

    def FlipImg(self, img):
        FlipImg = []
        dst = cv2.flip(img, 1)
        dst2 = cv2.flip(dst, 0)
        FlipImg.append(dst)
        FlipImg.append(dst2)

        dst = cv2.flip(img, 0)
        dst2 = cv2.flip(dst, 1)
        FlipImg.append(dst)
        FlipImg.append(dst2)

        cnt = 0
        for j in range(len(FlipImg)):
            # rotation filename
            filename = os.path.join(savepath, '{}_F_{}.jpg'.format(self.name,cnt))
            cv2.imwrite(filename,FlipImg[j])
            cnt += 1
        print('F')

    def MoveImg(self,img):
        aff = np.array([[1, 0, 200],
                        [0, 1, 100]], dtype=np.float32)

        dst = cv2.warpAffine(img, aff, (random.random(), random.random()),borderMode=cv2.BORDER_REPLICATE)
        cv2.imshow("112", dst)

if __name__ == '__main__':
    ImgDA = DataAugmentation()
    # ImgDA.FlipImg(img)
    # ImgDA.RotationImage(img)
    ImgDA.MoveImg(img)
    cv2.imshow("src", img)
    # cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





