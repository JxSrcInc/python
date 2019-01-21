from main import training
from main import test
from main import load_mnist

img_images, img_labels, tst_images, tst_labels = load_mnist()
print(img_images.shape)
clf = training(img_images, img_labels, 500)
test_size = 100
num_correct = test(clf, tst_images, tst_labels, test_size)
print ("Baseline classifier using an SVM.")
print ("%s of %s values correct." % (num_correct, test_size))

