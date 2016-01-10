import unittest
import logging

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
        print cls._settings

    def setUp(self):
        pass
#        if self.page_i==0 or self.page_j ==0:
#            raise unittest.SkipTest("Zero pages are not tested")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

