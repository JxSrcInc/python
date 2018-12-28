import sys
sys.path.insert(0, '../imglib')

import imgUtil as util
import cv2

winImg = util.createImage((600,1000),(0,0,255, 1.0))
font = ("simsun.ttc", 100, (255,255,255))

x = 100
y = 60
for text in ['中国','江西',"萍乡","1929年"]:
    print(y)
    winImg = util.overlayChineseWithFont(winImg, (x,y), text, font)
    h, w = util.chineseTextSize(text, font)
    y += h + 20
    x += w - 80
font = (cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
winImg = util.overlayTextWithFont(winImg, (x-100,y-60), '. . . . . .', font)
cv2.imshow("win", winImg)
cv2.waitKey()
#cv2.imshow("res", img)
#cv2.waitKey()
cv2.destroyAllWindows
cv2.imwrite('first.jpg',winImg)

