import unittest
from cases import DefaultTest
from importlib import import_module


def test_generator(settings):
    test_cases = unittest.TestSuite()
    cases = import_module(settings['cases'])
    for case_name in settings['include']:
        TestClass = cases.__getattribute__(case_name)
        setattr(TestClass,'_settings',settings)
        for p1, p2 in [(1, 2), (3, 4)]:
            test_cases.addTest(TestClass('equality', p1, p2))
    def load_tests(loader, tests, pattern):
    # FIXME: declare me as a decorator
        return test_cases

    return load_tests


"""

pdf_im = pyPdf.PdfFileReader(file('multi_page.pdf', "rb"))
npage = pdf_im.getNumPages()
for p in npage:
    im = PythonMagick.Image('multi_page.pdf['+ str(p) +']')
    im.write('file_out-' + str(p)+ '.png')
"""
