import unittest
import subprocess

class Core(unittest.TestCase):

    def target(self,command): 
        output = subprocess.check_output(command.split())
        result = eval(output)
        return result

    def test_identity(self):
        command = "python loaddb.py data/test/A.pdf data/test/A.pdf"
        subprocess.call(command.split())
        command = "python inspection.py data/test/A.pdf data/test/A.pdf"
        command = "python inspection.py"
        expect = [ (1,1),
                   (2,2),
                   (3,3),
                   (4,4),
                   (5,5),
                   (6,6),
                   (7,7),
                   (8,8),
                   (9,9), 
                   (10,10), ]
        result = self.target(command)
        self.assertEqual(expect,result)


if __name__ == '__main__':
    unittest.main()

