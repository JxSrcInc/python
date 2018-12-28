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
    
def overlayTextWithFont(image,
                startXY,
                text,
                fontInfo,
                alpha = 1):
    fontFace, fontScale, color, thickness = fontInfo
    return overlayText(image, startXY, text, 
                       fontFace, fontScale, color, alpha, thickness)
    
def overlayText(image, # nparray
                startXY, # (y, x) upper-left point
                text, # string
                fontFace, # cv2 FONT TYPE choice -> https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html#puttext
                fontScale, # int
                color, # (blue, grenn, red)
                alpha, # between 0 and 1
                thickness # positive int
                ):
    # create two copies of the original image -- one for
	# the overlay and one for the final output image
    overlay = image.copy()
    output = image.copy()
    size = cv2.getTextSize(text, fontFace, fontScale, thickness)
    # size = ((text-width, textHeight), line-height-text_height
    # adjust y to y+text_height. 
    # because in input arg startXY is upper-left point
    text_height = size[0][1]
    x, y = startXY
    startXY = (x, y+text_height)
    cv2.putText(overlay, text,
                startXY, fontFace, fontScale, color, thickness)
    cv2.addWeighted(overlay, alpha, output, 1-alpha,
                0, output)
    return output

def overlayChineseWithFont(image,
                startXY,
                text,
                fontInfo):
    fontFace, fontScale, color = fontInfo
    return overlayChinese(image, startXY, text,
                       fontFace, fontScale, color)

def overlayChinese(background,
        startXY, # upper-left point
        txt, 
        fontFace, # PIL ImageFont: example "simsun.ttc" 
        fontScale,
        color # (blue, green, red, alpha)
        ):
    txtLen = len(txt)
    width = txtLen*fontScale
    img = np.zeros((fontScale,width,4),np.uint8)
    
    font = ImageFont.truetype(fontFace, fontScale)

    img_pil = Image.fromarray(background)

    draw = ImageDraw.Draw(img_pil)
    # NOTE: startXY in PIL is upper-left, 
    # which is different from cv2's bottom left 
    draw.text( startXY, txt, font=font, fill=color)
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

def textSize(text, font):
    fontFace, fontScale, color, thickness = font
    size = cv2.getTextSize(text, fontFace, fontScale, thickness)
    return (size[0][1]+size[1], size[0][0])

def chineseTextSize(text, font):
    fontFace, fontScale, color = font
    txtLen = len(text)
    return (fontScale, txtLen*fontScale)



