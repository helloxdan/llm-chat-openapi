#coding=utf-8
# 改变图片的分辨率大小

import os  #打开文件时需要
from PIL import Image
import re

CURRENT_PATH = os.getcwd()  # 获取当前路径
UPLOAD_FOLDER = CURRENT_PATH + '\\img_upload\\'
NEW_FOLDER=CURRENT_PATH + "\\img_dlib\\"
MIN_W=640.0
MAX_W=2016.0
MIN_H=480.0
MAX_H=3840.0
STA_W=1024.0
STA_H=768.0
files= os.listdir(UPLOAD_FOLDER) #得到文件夹下的所有文件名称
for file in files:
    img=Image.open(UPLOAD_FOLDER+file)
    w,h=img.size
    if w<MIN_W or w>MAX_W or h<MIN_H or h>MAX_H:
        new_w=STA_H*float(w/h)
        new_h=STA_W*float(h/w)
        out = img.resize((int(new_w),int(new_h)),Image.ANTIALIAS)
        new_pic=re.sub(file[:-4],file[:-4]+'_new',file)
        out.save(NEW_FOLDER+new_pic)
