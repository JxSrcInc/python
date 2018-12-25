import sys
sys.path.insert(0, '../imglib')

import imgUtil as util
import cv2
import numpy as np


winImg = util.createImage((200,300),(0,0,255, 1.0))
winImg = util.overlayChinese('中国',winImg, 100, (255,255,255))
cv2.imshow("win", winImg)
cv2.waitKey()
#cv2.imshow("res", img)
#cv2.waitKey()
cv2.destroyAllWindows

