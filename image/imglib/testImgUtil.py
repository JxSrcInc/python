import imgUtil as util
import cv2

def testOverlayText(img, text, startXY):
    fontInfo = (cv2.FONT_HERSHEY_SIMPLEX,10,(0,0,0),10)
    nImg = util.overlayTextWithFont(img, startXY, text, fontInfo, 0.5)
    return nImg

def testOverlayImage(img, overlayImg): 
    overlayImg = util.resizeByScale(overlayImg, 0.5)
    nImg = util.overlayImage(img, overlayImg, (0,0), 0.5)
    return nImg

def testResize():
    img = cv2.imread('./resources/TEST.JPG',cv2.IMREAD_COLOR)
    return util.resizeByScale(img)
    
def display(img, filename='test.jpg'):
    print(img.shape)
    cv2.imwrite(filename,img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def testOverlayChinese(img, text, startXY):
    font = ("simsun.ttc", 300, (0,0,255))
    nImg = util.overlayChineseWithFont(img, startXY, text, font)
    return nImg

def test():
    img = cv2.imread('./resources/TEST.JPG',cv2.IMREAD_COLOR)
    overlayImg = cv2.imread('./resources/TEST1.JPG',cv2.IMREAD_COLOR)
    img = testOverlayImage(img, overlayImg)
    img = testOverlayChinese(img, '波士顿', (0,0))
    img = testOverlayText(img, 'Boston', (300,300))
    display(img)
print(util.chineseTextSize('波士顿', ("simsun.ttc", 300, (0,0,255))))
print(util.textSize('message', (cv2.FONT_HERSHEY_TRIPLEX, 10, (0,0,255),1)))
test()

