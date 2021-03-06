import numpy as np
import cv2

class ImagePrinter:

    """
    cells format: (cellsInHeight, cellsInWidth)
    
    """
    def __init__(self, cells, background, file="image"):
        self.background = background 
        self.file = file
        # image size is 28, cellsize = image size + 1
        self.cellsize = 29
        hcells, wcells = cells
        self.imgSrc = np.zeros((hcells*self.cellsize,wcells*self.cellsize))
        self.imgTest = np.zeros((hcells*self.cellsize,wcells*self.cellsize))
        self.imgSrc.fill(self.background)
        self.imgTest.fill(self.background) 
        self.hcnt = 0
        self.wcnt = 0
        self.hcells = hcells
        self.wcells = wcells

    """
    Select "self.hcells*self.wcells" random number 
    from a range of size (default to 10000)
    
    TODO: need refine
    """
    def displayIndexes(self, size=10000):    
        indexes = np.zeros(size)
        for i in range(self.hcells*self.wcells):
            index = int(np.random.uniform()*(size-1))
            indexes[index] = 1
        return indexes
        
    """
    Add an image to printer
    """
    def addCellImg(self, imgSrc, imgTest):
        imgSrc = imgSrc.reshape((28,28))
        imgTest = imgTest.reshape((28,28))
        x = self.cellsize*self.wcnt
        y = self.cellsize*self.hcnt
        self.imgSrc[y:y+28,x:x+28] = imgSrc
        self.imgTest[y:y+28,x:x+28] = imgTest
        self.wcnt += 1
        if self.wcells == self.wcnt:
            self.wcnt = 0
            if self.hcnt < self.hcells-1:
                self.hcnt += 1
    
    """
    print all added images
    """
    def printImg(self):
        self.printHorizontal()
        
    """
    print two image sets vertcally
    """
    def printVertical(self):
        img = np.zeros((self.hcells*self.cellsize*2+10,self.wcells*self.cellsize))
        img.fill(self.background)
        img[0:self.hcells*self.cellsize,0:self.wcells*self.cellsize] = self.imgSrc
        img[self.hcells*self.cellsize+10:self.hcells*self.cellsize*2+10,
            0:self.wcells*self.cellsize] = self.imgTest
        self.output(img)

    """
    print two image sets horizontally
    """
    def printHorizontal(self):
        img = np.zeros((self.hcells*self.cellsize,self.wcells*self.cellsize*2+10))
        img.fill(self.background)
        img[0:self.hcells*self.cellsize,0:self.wcells*self.cellsize] = self.imgSrc
        img[0:self.hcells*self.cellsize,self.wcells*self.cellsize+10:self.wcells*self.cellsize*2+10] = self.imgTest
        self.output(img)        

    def printFirst(self):
        img = np.zeros((self.hcells*self.cellsize,self.wcells*self.cellsize))
        img.fill(self.background)
        img[0:self.hcells*self.cellsize,0:self.wcells*self.cellsize] = self.imgSrc
        self.output(img)
        
    def output(self, img, title="original and modified test samples"):
 #       img = cv2.imread("C:\git\python\image\90anniversary\first.jpg")
        cv2.imshow(title,img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        img = img*255
        cv2.imwrite(self.file+'.png',img)

