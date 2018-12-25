from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

# color = (int, int, int): (blue, green, red)
# color = (int, int, int, alpha): (blue, green, red, alpha)
def createImage(rectangle, color):
    h, w = rectangle
    size = len(color)
    img = np.zeros((h,w,size), np.uint8)
    img[0:h,0:w] = color
    return img

def addAlphaChanel(img):
    h, w, d = img.shape
    _img = img
    if d == 3:
        img = np.ones((h,w,4),np.uint8)
        img[0:h,0:w,0:3] = _img
    if d == 1:
        img = np.zeros((h,w,2),np.uint8)
        img[0:h,0:w,0:1] = _img
    return img
    
def overlayText(image, # nparray
                text, # string
                alpha, # between 0 and 1
                startXY, # (y, x) bottom-left point
                fontFace, # cv2 FONT TYPE choice -> https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html#puttext
                fontScale, # int
                color, # (blue, grenn, red)
                thickness # positive int
                ):
    # create two copies of the original image -- one for
	# the overlay and one for the final output image
    overlay = image.copy()
    output = image.copy()
    cv2.putText(overlay, text,
                startXY, fontFace, fontScale, color, thickness)
    cv2.addWeighted(overlay, alpha, output, 1-alpha,
                0, output)
    return output

def overlayChinese(txt, background,
        fontSize=36,
        fontColor=(0,0,0), # (blue, green, red, alpha)
        startXY=(0,0), # upper-left point
        fontpath = "simsun.ttc" ## Use simsum.ttc to write Chinese.
        ):
    print(fontColor)
    txtLen = len(txt)
    width = txtLen*fontSize
    img = np.zeros((fontSize,width,4),np.uint8)
    
    font = ImageFont.truetype(fontpath, fontSize)

    img_pil = Image.fromarray(background)

    draw = ImageDraw.Draw(img_pil)
    # NOTE: startXY in PIL is upper-left, 
    # which is different from cv2's bottom left 
    draw.text( startXY, txt, font=font, fill=fontColor)
    img = np.array(img_pil)
#    print(img.shape[1])
    return img


def overlayImage(image, # nparray
                overlay, # nparray
                startXY, # (y, x) - upper-left point
                alpha):
    # create two copies of the original image -- one for
	# the overlay and one for the final output image
    src = image.copy()
    output = image.copy()
    h, w, d = overlay.shape
    y, x = startXY
    src[y:y+h, x:x+w] = overlay
    cv2.addWeighted(src, alpha, output, 1-alpha,
                0, output)
    return output

def resizeByScale(img, scale=0.5):
    h, w, d = img.shape
    h = int(h*scale)
    w = int(w*scale)
    return cv2.resize(img, (w,h))


