import frameworks
import cv2
import cv
import numpy
import unittest


class DefaultTest(frameworks.PNGs):
    def equality(self):
        equal = numpy.array_equal(self.image_i, self.image_j)
        self.assertTrue(equal)


class MyTest1(frameworks.PNGs):
    def gray_histogram_cmp_corr(self):
        threshold = .9

        gray_i = cv2.cvtColor(self.image_i,cv2.COLOR_BGR2GRAY)
        hist_i = cv2.calcHist([gray_i],[0],None,[256],[0,256])

        gray_j = cv2.cvtColor(self.image_j,cv2.COLOR_BGR2GRAY)
        hist_j = cv2.calcHist([gray_j],[0],None,[256],[0,256])

        measure = cv2.compareHist(hist_i, hist_j, cv.CV_COMP_CORREL) 
        self.assertGreater(measure,threshold)

    def equality(self):
        if self.page_i==0 or self.page_j ==0:
            raise unittest.SkipTest("Don't run this test on the first pages")
        equal = numpy.array_equal(self.image_i, self.image_j)
        self.assertTrue(equal)


class MyTest2(frameworks.PNGs):
    def gray_histogram_cmp_bhatta(self):
        threshold = .9

        gray_i = cv2.cvtColor(self.image_i,cv2.COLOR_BGR2GRAY)
        hist_i = cv2.calcHist([gray_i],[0],None,[256],[0,256])

        gray_j = cv2.cvtColor(self.image_j,cv2.COLOR_BGR2GRAY)
        hist_j = cv2.calcHist([gray_j],[0],None,[256],[0,256])

        measure = cv2.compareHist(hist_i, hist_j, cv.CV_COMP_BHATTACHARYYA) 
        self.assertGreater(measure,threshold)

