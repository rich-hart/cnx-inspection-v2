import unittest
import inspection
import subprocess

DATABASE = "temp-png-testing"
USER = "qa"
PDF_A = "data/A.pdf"
PDF_B = "data/B.pdf"
OUTPUT_LOG = "data/output.log"
RESULTS_LOG = "data/results.log" 
CASE_MODULE = "data/dummy_cases.py"
INCLUDE = ['MyTest_1','MyTest_2']
EXCLUDE = ['DefaultTest']

class TestCore(unittest.TestCase):
     def test_main(self):
         command = "python inspection.py --include MyTest_1 --include MyTest_2 --exclude DefaultTest --cases data/dummy_cases.py"
         output = subprocess.check_output("python inspection.py --include MyTest_1 --include MyTest_2 --exclude DefaultTest".split())
         print("\n\n" + output)


class TestUtils(unittest.TestCase):
    pass
