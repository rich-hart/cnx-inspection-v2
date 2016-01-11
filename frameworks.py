import unittest
import logging
import psycopg2
import cv2
import cv
import numpy
class PNGs(unittest.TestCase):
    def __init__(self, methodName, page_i=0, page_j=0):
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

    def setUp(self):
        with self._connection.cursor() as cur:
            cur.execute("SELECT Data FROM png_a WHERE Page={0}".format(self.page_i))
            data = numpy.asarray(cur.fetchone()[0])
            self.image_i = cv2.imdecode(data,cv.CV_LOAD_IMAGE_COLOR)
            cur.execute("SELECT Data FROM png_b WHERE Page={0}".format(self.page_j))
            data = numpy.asarray(cur.fetchone()[0])
            self.image_j = cv2.imdecode(data,cv.CV_LOAD_IMAGE_COLOR)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

