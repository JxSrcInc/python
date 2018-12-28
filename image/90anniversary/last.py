import sys
sys.path.insert(0, '../imglib')

import imgUtil as util
import cv2

imgH = 600
imgW = 1000
winImg = util.createImage((imgH, imgW),(0,0,255, 1.0))
font140 = ("simsun.ttc", 140, (255,255,255))
font60 = ("simsun.ttc", 60, (255,255,255))

src = [("爸爸生日快乐",font140,20),("我们爱您",font140,80),
       ("张小莽 张青青 张南南",font60,1),("范翼中 季红俊 李 江",font60,0)]
y = 70
for text, font, skip in src:
    h, w = util.chineseTextSize(text, font)
    x = int((imgW-w)/2)
    winImg = util.overlayChineseWithFont(winImg, (x,y), text, font)
    y += h+skip

cv2.imshow("win", winImg)
cv2.waitKey()
#cv2.imshow("res", img)
#cv2.waitKey()
cv2.destroyAllWindows

cv2.imwrite("last.jpg",winImg)

