import unittest
from cases import DefaultTest



def test_generator(settings):
    test_cases = unittest.TestSuite()
    setattr(DefaultTest,'_settings',settings)
    for p1, p2 in [(1, 2), (3, 4)]:

        test_cases.addTest(DefaultTest('equality', p1, p2))

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
