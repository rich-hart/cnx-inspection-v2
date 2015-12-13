import unittest
from cases import DefaultTest

#def load_png_tests(loader, tests, pattern):

#    test_cases = unittest.TestSuite()
#    for p1, p2 in [(1, 2), (3, 4)]:
#        test_cases.addTest(DefaultTest('equality', p1, p2))
#    return test_cases


def test_generator(settings):
    test_cases = unittest.TestSuite()
    for p1, p2 in [(1, 2), (3, 4)]:
        test_cases.addTest(DefaultTest('equality', p1, p2))

    def load_tests(loader, tests, pattern):
        return test_cases

    return load_tests

