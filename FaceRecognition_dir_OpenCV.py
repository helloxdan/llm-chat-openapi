import os
import cv2

PATH = "img_upload"
NEWPATH="img_cv"
files= os.listdir(PATH) #得到文件夹下的所有文件名称  
s = [] 
# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "data\\haarcascades\\haarcascade_frontalface_default.xml"
)
for file in files: #遍历文件夹  
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
        img = cv2.imread(PATH+"/"+file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转换灰色
        faceRects = classifier.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(32, 32))# 调用识别人脸
        if len(faceRects):  # 大于0则检测到人脸
            num=1
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                crop_img = img[y:y + h, x:x + w]
                cv2.imwrite(NEWPATH+"/"+str(num)+file, crop_img) # 框出人脸
                num +=1
cv2.waitKey(0)
cv2.destroyAllWindows()