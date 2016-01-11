import frameworks
import cv2
import cv
import numpy
class DefaultTest(frameworks.PNGs):
    def equality(self):
        equal = numpy.array_equal(self.image_i, self.image_j)
        self.assertTrue(equal)

class MyTest1(frameworks.PNGs):
    def histogram_cmp_corr(self):
        pass

    def equality(self):
        if self.page_i==0 or self.page_j ==0:
            raise unittest.SkipTest("Don't run this test on the first pages")
        equal = numpy.array_equal(self.image_i, self.image_j)
        self.assertTrue(equal)

class MyTest2(frameworks.PNGs):
    def histogram_cmp_bhatta(self):
        self.threshold = .2


