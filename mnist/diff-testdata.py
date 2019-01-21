from main import training
from main import test
from main import load_mnist
import util

img_images, img_labels, tst_images, tst_labels = load_mnist()
md_tst_images = util.modifyData(tst_images, 0)
clf = training(img_images, img_labels, 500)
test_size = 100
num_correct = test(clf, tst_images, tst_labels, test_size)
print ("Baseline classifier using an SVM.")
print ("%s of %s values correct." % (num_correct, test_size))
num_correct = test(clf, md_tst_images, tst_labels, test_size)
print ("Modified test data classifier using an SVM.")
print ("%s of %s values correct." % (num_correct, test_size))
