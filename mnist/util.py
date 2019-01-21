import image
import numpy as np

"""
Select first 100 images from srs according to nmbr
"""
def select_image(src, nmbr, file="image"):
    printer = image.ImagePrinter((10,10),0.5,file)
    x, y = src
    size = len(x)
    cnt = 0;
    for i in range(size):
        if y[i] == nmbr and cnt < 100:
            print(i)
            img = x[i].copy()
            for k in range(len(img)):
                img[k] = 1 - img[k]
            cnt += 1
            printer.addCellImg(x[i], img)
    printer.printFirst()

"""
Revert the grayscale of an image
"""
def modifySample(src):
    x, y = src
    x1 = modifyData(x)
    return (x1,y)

def modifyData(x, thread):
    x1 = np.array(x)
    # y is an element based on the first dimention of X1
    x2 = [1 - y for y in x1]
    return x2
    # need convert to np array
    #return np.array(x2)

"""
Randomly selete image pair using image.ImagePrinter:
one from origin and one from modified based on index

Requirement: origin and modified must have the same size and the same order
For example, if origin[index] represents 6, then modified[index] must also represnet 6
"""
def extractImage(origin, modified, file="image"):
    printer = image.ImagePrinter((10,10),0.5,file)
    imgSrc = origin;
    imgTest = modified;
    size = len(imgSrc)
    print("sample size = %d"%size)
    display_index = printer.displayIndexes(size)
    cnt = 0
    for i in range(size):
#        assert(labelSrc[i] != labelSrc[i]), "labelSrc=%d, labelTest=%d" % (labelSrc[i],labelTest[i])
        if display_index[i] > 0:
            cnt += 1
            printer.addCellImg(imgSrc[i], imgTest[i])
    print("select images = %d" % (cnt))
    printer.printImg()

"""
Select subarray of size from MNIST images and labels
Convert them from 3D to 2D for nueral networks machine learning using "sklearn" package
"""
def mnistConv(src_images, src_labels):
    size = src_labels.size
    #imgs = np.zeros((size, 28*28), np.float)
    imgs = np.reshape(src_images[0:size,:,:],(size,28*28))
    #for i in range(size):
    #    imgs[i,:] = _imgs[i,:]/255
    imgs = imgs/255
    return (imgs, src_labels)

def subSample(src_images, src_labels, size):
    if(size > src_labels.size):
        size = src_labels.size

    # select the first 'size' elements according to the first dimention
    labels = src_labels[0:size]
    images = src_images[0:size]
    
    return(images, labels)
    
    