import unittest
from cases import DefaultTest

def load_png_tests(loader, tests, pattern):

    test_cases = unittest.TestSuite()
    for p1, p2 in [(1, 2), (3, 4)]:
        test_cases.addTest(DefaultTest('equality', p1, p2))
    return test_cases

def parse_log(log):
    pass


