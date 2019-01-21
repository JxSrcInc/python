from main import load_mnist
import util

img_images, img_labels, tst_images, tst_labels = load_mnist()
md_tst_images = util.modifyData(tst_images, 0)
util.extractImage(tst_images, md_tst_images)
