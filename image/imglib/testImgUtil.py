import imgUtil as util
import cv2

def testOverlayText(img):
    nImg = util.overlayText(img,"Test Message",0.5,(10,200),
                            cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,255),5)
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
    
def testOverlayChinese(img):
    nImg = util.overlayChinese('波士顿', img, 300, (0,0,255))
    return nImg

def test():
    img = cv2.imread('./resources/TEST.JPG',cv2.IMREAD_COLOR)
    overlayImg = cv2.imread('./resources/TEST1.JPG',cv2.IMREAD_COLOR)
    img = testOverlayImage(img, overlayImg)
    img = testOverlayChinese(img)
    display(img)
    
test()

