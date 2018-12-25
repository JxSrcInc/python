import cv2
import numpy as np
from imgWrap import Img

def creatImg(topImgFile, bottomImgFile, height, width):
    i = cv2.imread(bottomImgFile,cv2.IMREAD_COLOR)
    bottomImg = Img(i)
    i = cv2.imread(topImgFile,cv2.IMREAD_COLOR)
    topImg = Img(i)
#    cv2.imshow('image',topImg.img)
#    cv2.waitKey(0)

#    topImg = Img(cv2.imread(topImgFile,cv2.IMREAD_COLOR))
#    bottonImg = Img(cv2.imread(bottomImgFile,cv2.IMREAD_COLOR))
    (b,g,r) = topImg.img[5,5]
    img = np.zeros((height,width,3),np.uint8)
    img[:,:,0] = b
    img[:,:,1] = g
    img[:,:,2] = r


    img = Img(img)
    y = int(topImg.height/2)
    nImg = img.draw(topImg.img, (y, int(width/2)))
    y = img.height-int(bottomImg.height/2)
    nImg = img.draw(bottomImg.img, (y, int(width/2)))
    return nImg
    
    
img = creatImg('./resources/heart.jpg','./resources/figure.jpg', 800,1000)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
