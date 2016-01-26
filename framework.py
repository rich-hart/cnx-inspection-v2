import unittest
import logging
import psycopg2
import cv2
import cv
import numpy
import sys
import exceptions
import PythonMagick
import contextlib
import utils

class PDFCV(unittest.TestCase):
    def __init__(self, methodName, page_i=1, page_j=1):
        testName = "{0}(page_i={1},page_j={2})".format(methodName,page_i,page_j)
        method = getattr(self,methodName) 
        setattr(self, testName, method)
        super(PDFCV, self).__init__(testName)
        self.page_i = page_i
        self.page_j = page_j
        self.methodName = methodName

    @classmethod
    def setUpClass(cls):
        cls._casename = cls.__name__
        cls._logger = logging.getLogger(cls._casename)        

    def setUp(self):
        if self.page_i==0 or self.page_j ==0:
            raise unittest.SkipTest("zero pages should be null")
        self.image_i=utils.load_pdf_page(self._settings['pdf_a'],self.page_i-1)
        self.image_j=utils.load_pdf_page(self._settings['pdf_b'],self.page_j-1)

    def tearDown(self):
        sys_info = sys.exc_info()
        result = None
        test_info = {}
        if sys_info == (None,None,None):
            result = "pass"
        elif isinstance(sys_info[1],exceptions.AssertionError):
            result = "fail"
        elif isinstance(sys_info[1],unittest.case.SkipTest):
            result = "skip"
        else:
            result = "error"

        test_info['result'] = result
        test_info['page_i'] = self.page_i
        test_info['page_j'] = self.page_j
        test_info['test'] = self.methodName
        test_info['case'] = self._casename
        self._logger.info(str(test_info))

    @classmethod
    def tearDownClass(self):
        pass

