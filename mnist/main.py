import mnist
# Third-party libraries
from sklearn import svm
import util

def load_mnist():
    img_images = mnist.train_images()
    img_labels = mnist.train_labels()
    tst_images = mnist.test_images()
    tst_labels = mnist.test_labels()
    
    img_images, img_labels = util.mnistConv(img_images, img_labels)
    tst_images, tst_labels = util.mnistConv(tst_images, tst_labels)
    print(tst_images.shape)
    print(img_images.shape)
    
    print("loaded data")
    return (img_images, img_labels, tst_images, tst_labels)
    
def training(img_images, img_labels, size):
    print("select samples %d" % size)
    training_images, training_labels = util.subSample(img_images, img_labels, size)
    print("start training (%d, %d)" % training_images.shape)
    
    # train
    clf = svm.SVC()
    clf.fit(training_images, training_labels)
    print("complete training")
    return clf

# test
def test(clf, tst_images, tst_labels, size):
    test_images, test_labels = util.subSample(tst_images, tst_labels, size)
    #print(test_images.shape)
    predictions = [int(a) for a in clf.predict(test_images)]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_labels))
    return num_correct

if __name__ == "__main__":
    img_images, img_labels, tst_images, tst_labels = load_mnist()
    clf = training(img_images, img_labels, 50000)
    test_size = 10000
    num_correct = test(clf, tst_images, tst_labels, test_size)
    print ("Baseline classifier using an SVM.")
    print ("%s of %s values correct." % (num_correct, test_size))
