import unittest

class PNGs(unittest.TestCase):
    def __init__(self, methodName, page_i=0, page_j=0):
        testName = "{0}(page_i={1},page_j={2})".format(methodName,page_i,page_j)
        method = getattr(self,methodName) 
        setattr(self, testName, method)
        super(PNGs, self).__init__(testName)
        self.page_i = page_i
        self.page_j = page_j
        self.methodName = methodName

    def runTest(self):
        pass  # Test that depends on param 1 and 2.



