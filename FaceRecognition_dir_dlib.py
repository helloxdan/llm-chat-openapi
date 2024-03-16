#coding=utf-8

import os
import dlib
import cv2

CURRENT_PATH = os.getcwd()  # 获取当前路径
PATH = CURRENT_PATH + "\\img_upload"
NEWPATH=CURRENT_PATH + "\\img_dlib"
files= os.listdir(PATH) #得到文件夹下的所有文件名称 
#人脸分类器
detector = dlib.get_frontal_face_detector()
for file in files: #遍历文件夹  
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
        img = cv2.imread(PATH+"/"+file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(gray, 1)
        print("识别到的人脸数量: {}".format(len(dets)))  # 打印识别到的人脸个数
        # enumerate是一个Python的内置方法，用于遍历索引
        # index是序号；face是dets中取出的dlib.rectangle类的对象，包含了人脸的区域等信息
        # left()、top()、right()、bottom()都是dlib.rectangle类的方法，对应矩形四条边的位置
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            crop_img = img[top:bottom, left:right]
            if index==0:
                newimgpath=NEWPATH+"/"+file
            else:
                newimgpath=NEWPATH+"/"+str(index+1)+file
            cv2.imwrite(newimgpath, crop_img) # 框出人脸
# 等待按键，随后退出，销毁窗口
k = cv2.waitKey(0)
cv2.destroyAllWindows()