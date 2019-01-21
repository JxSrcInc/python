import main
import util
from sklearn import svm

def svm_baseline():
    img_images, img_labels, tst_images, tst_labels = main.load_mnist()
    training_images, training_labels = util.subSample(img_images, img_labels, 50000)
    training_data = (training_images, training_labels)
    test_data = (tst_images, tst_labels)
    print(training_data[0].shape)
    print(training_data[1].shape)
    print(test_data[0].shape)
    print(test_data[1].shape)
    # train
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    # test
    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print( "Baseline classifier using an SVM.")
    print( "%s of %s values correct." % (num_correct, len(test_data[1])))

if __name__ == "__main__":
    svm_baseline()
    
