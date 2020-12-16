import cv2
import os
import numpy as np




# 좌표값은 이미지의 비율로 들어가있기 때문에 따로 읽어오는 방법이 필요하다
def yoloFormattocv(x1, y1, x2, y2, H, W):
    bbox_width = x2 * W
    bbox_height = y2 * H
    center_x = x1 * W
    center_y = y1 * H
    voc = []
    voc.append(center_x - (bbox_width / 2))
    voc.append(center_y - (bbox_height / 2))
    voc.append(center_x + (bbox_width / 2))
    voc.append(center_y + (bbox_height / 2))
    return [int(v) for v in voc]

def cvFormattoYolo(corner, H, W):
    bbox_W = corner[3] - corner[1]
    bbox_H = corner[4] - corner[2]

    center_bbox_x = (corner[1] + corner[3]) / 2
    center_bbox_y = (corner[2] + corner[4]) / 2

    return corner[0], round(center_bbox_x / W, 6), round(center_bbox_y / H, 6), round(bbox_W / W, 6), round(bbox_H / H,
                                                                                                            6)

class yoloRotatebbox:
    def __init__(self, filename, image_ext, angle):
        # assert 보증하다다 : 예외 처리할 때 쓰인다
        # isfile이 아닐경울 error를 발생한
        assert os.path.isfile(filename + image_ext)
        assert os.path.isfile(filename + '.txt')

        # 파일 이름
        self.filename = filename
        # 파일 확장자
        self.image_ext = image_ext
        self.angle = angle

        # Read image using cv2
        self.image = cv2.imread(self.filename + self.image_ext, 1)

        # create a 2D-rotation matrix
        rotation_angle = self.angle * np.pi / 180
        self.rot_matrix = np.array(
            [[np.cos(rotation_angle), -np.sin(rotation_angle)], [np.sin(rotation_angle), np.cos(rotation_angle)]])

    # 이미지 돌리기
    def rotate_image(self):
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        """
        height, width = self.image.shape[:2]  # image shape has 3 dimensions
        image_center = (width / 2,
                        height / 2)  # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

        rotation_mat = cv2.getRotationMatrix2D(image_center, self.angle, 1.)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat[0, 0])
        abs_sin = abs(rotation_mat[0, 1])

        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)

        # subtract old image center (bringing image back to origin) and adding the new image center coordinates
        rotation_mat[0, 2] += bound_w / 2 - image_center[0]
        rotation_mat[1, 2] += bound_h / 2 - image_center[1]

        # rotate image with the new bounds and translated rotation matrix
        rotated_mat = cv2.warpAffine(self.image, rotation_mat, (bound_w, bound_h))
        return rotated_mat

    # bounding box 돌리기
    def rotateYolobbox(self):
        # 돌린 이미지의 높이, 넓이
        new_height, new_width = self.rotate_image().shape[:2]
        # 좌표값이 적혀져있는 txt 파일 불러오기
        f = open(self.filename + '.txt', 'r')

        f1 = f.readlines()

        new_bbox = []
        # 원본이미지의 높이,넓이
        H, W = self.image.shape[:2]

        for x in f1:
            # 파일을 불러올 때 \n도 같이 불러들이는데 \n은 잘라내고 띄어쓰기 부분으로 split
            bbox = x.strip('\n').split(' ')
            if len(bbox) > 1:
                (center_x, center_y, bbox_width, bbox_height) = yoloFormattocv(float(bbox[1]), float(bbox[2]),
                                                                               float(bbox[3]), float(bbox[4]), H, W)

                # shift the origin to the center of the image.
                upper_left_corner_shift = (center_x - W / 2, -H / 2 + center_y)
                upper_right_corner_shift = (bbox_width - W / 2, -H / 2 + center_y)
                lower_left_corner_shift = (center_x - W / 2, -H / 2 + bbox_height)
                lower_right_corner_shift = (bbox_width - W / 2, -H / 2 + bbox_height)

                new_lower_right_corner = [-1, -1]
                new_upper_left_corner = []

                for i in (upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift,
                          lower_right_corner_shift):
                    new_coords = np.matmul(self.rot_matrix, np.array((i[0], -i[1])))
                    x_prime, y_prime = new_width / 2 + new_coords[0], new_height / 2 - new_coords[1]
                    if new_lower_right_corner[0] < x_prime:
                        new_lower_right_corner[0] = x_prime
                    if new_lower_right_corner[1] < y_prime:
                        new_lower_right_corner[1] = y_prime

                    if len(new_upper_left_corner) > 0:
                        if new_upper_left_corner[0] > x_prime:
                            new_upper_left_corner[0] = x_prime
                        if new_upper_left_corner[1] > y_prime:
                            new_upper_left_corner[1] = y_prime
                    else:
                        new_upper_left_corner.append(x_prime)
                        new_upper_left_corner.append(y_prime)
                #             print(x_prime, y_prime)

                new_bbox.append([int(bbox[0]), new_upper_left_corner[0], new_upper_left_corner[1],
                                 new_lower_right_corner[0], new_lower_right_corner[1]])


        return new_bbox


path ="/home/ubuntu/bit/Yolo_mark/x64/Release/data/img/air1"
FileDir = '/home/ubuntu/bit/Yolo_mark/x64/Release/data/img'
FileList = os.listdir(FileDir)
# 확장자가 jpg인 파일이름들만 가지고 온
JpgFile=[file for file in FileList if file.endswith('.jpg')]
ClassName = 'air'
ext = '.jpg'


if __name__ =='__main__':

    cnt =1

    SaveImgList=[]
    SaveTxtList=[]
    idx = 0

    for i in range(0,360,15):
        Img = yoloRotatebbox(path,ext,i)
        # image
        RoteImg = Img.rotate_image()
        # txt
        RoteTxt = Img.rotateYolobbox()

        SaveImgList.append(RoteImg)
        SaveTxtList.append(RoteTxt)


    for i in SaveImgList:
        #이
        NameI = ClassName + '{}.jpg'.format(cnt)
        NameF = ClassName + '{}.txt'.format(cnt)

        Savepath = os.path.join(FileDir, NameI)
        Savepath2 = os.path.join(FileDir, NameF)


        while 1:
            if os.path.isfile(Savepath):
                cnt +=1
                NameI = ClassName + '{}.jpg'.format(cnt)
                Savepath = os.path.join(FileDir, NameI)

                NameF = ClassName + '{}.txt'.format(cnt)
                Savepath2 = os.path.join(FileDir, NameF)

            else:
                break

        # txtW = ''
        # for axis in SaveTxtList[idx][0]:
        #     txtW = txtW + str(axis) + ' '
        # #print(txtW)

        f = open(Savepath2,'w')
        # f.writelines(' '.join(map(str, cvFormattoYolo(i, saveimg.shape[0], saveimg.shape[1]))) + '\n')
        # f.close()
        with open(Savepath2, 'a') as fout:
            fout.writelines(
                ' '.join(map(str, cvFormattoYolo(SaveTxtList[idx][0], i.shape[0], i.shape[1]))) + '\n')
        idx+=1
        cv2.imwrite(Savepath, i)



    cv2.imshow('Img', RoteImg)
    cv2.waitKey()
    cv2.destroyAllWindows()












