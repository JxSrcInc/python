class Img:
    def __init__(self, img):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1]
    def center(self):
        return (self.height/2, self.width/2)

    def topCenter(self):
        return (0, self.width/2)
    
    def bottomCenter(self):
        return (self.height, self.width/2)
    
    def leftCenter(self):
        return(self.height/2, 0)
        
    def rightCenter(self):
        return (self.height/2, self.widtd)
    
    def getRectangle(self, tl, br):
        tly, tlx = tl
        bry, brx = br
        x0 = max(0, tlx)
        x1 = min(brx, self.width)
        y0 = max(0, tly)
        y1 = min(bry, self.height)
        return self.img[y0:y1, x0:x1]
    
    # assum img is small than this image
    def draw(self, img, loc):
        y, x = loc
        img = Img(img)
        if y < int(img.height/2):
            y = int(img.height/2)
        if x < int(img.width/2):
            x = int(img.width/2)
        h0 = y - int(img.height/2)
        h1 = h0 + img.height
        w0 = x - int(img.width/2)
        w1 = w0 + img.width
        self.img[h0:h1, w0:w1] = img.img
        return self.img
        
        
