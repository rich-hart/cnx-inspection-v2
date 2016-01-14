import unittest
import logging
import psycopg2
import cv2
import cv
import numpy
import sys
import exceptions

# NOTE: consider loading all images into memory depending on system resources

class PNGs(unittest.TestCase):
    def __init__(self, methodName, page_i=1, page_j=1):
        testName = "{0}(page_i={1},page_j={2})".format(methodName,page_i,page_j)
        method = getattr(self,methodName) 
        setattr(self, testName, method)
        super(PNGs, self).__init__(testName)
        self.page_i = page_i
        self.page_j = page_j
        self.methodName = methodName

    @classmethod
    def setUpClass(cls):
        cls._connection = psycopg2.connect(database=cls._settings['database'])
        cls._casename = cls.__name__
        cls._logger = logging.getLogger(cls._casename)
    def setUp(self):
        if self.page_i==0 or self.page_j ==0:
            raise unittest.SkipTest("zero pages should be null")

        self.class_vars = None
        self.class_vars = self.__dict__
        with self._connection.cursor() as cur:
            cur.execute("SELECT Data FROM png_a WHERE Page={0}".format(self.page_i))
            data = numpy.asarray(cur.fetchone()[0])
            self.image_i = cv2.imdecode(data,cv.CV_LOAD_IMAGE_COLOR)
            cur.execute("SELECT Data FROM png_b WHERE Page={0}".format(self.page_j))
            data = numpy.asarray(cur.fetchone()[0])
            self.image_j = cv2.imdecode(data,cv.CV_LOAD_IMAGE_COLOR)

# FIXME: Have way for tearDown method, obtain any save value from test
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

