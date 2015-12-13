import unittest
import inspection
import subprocess
class TestCore(unittest.TestCase):
     def test_main(self):
         output = subprocess.check_output("python inspection.py --include MyTest_1 --include MyTest_2 --exclude DefaultTest".split())
         print("\n\n" + output)
