import unittest
import subprocess

class Core(unittest.TestCase):

    def target(self,load,run): 
        p=subprocess.Popen(load.split())
        p.wait()
        output = subprocess.check_output(run.split())
        result = eval(output)
        return result

    def test_identity(self):
        load = "python loaddb.py data/test/A.pdf data/test/A.pdf"
        run = "python inspection.py"
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
        result = self.target(load,run)
        self.assertEqual(expect,result)

    def test_page_removed(self):
        load = "python loaddb.py data/test/A.pdf data/test/B.pdf"
        run = "python inspection.py"
        expect = [ (1,1),
                   (2,2),
                   (4,3),
                   (5,4),
                   (6,5),
                   (7,6),
                   (8,7),
                   (9,8), 
                   (10,9), ]
        result = self.target(load,run)
        self.assertEqual(expect,result)

        load = "python loaddb.py data/test/B.pdf data/test/A.pdf"
        run = "python inspection.py"
        expect = [ (1,1),
                   (2,2),
                   (3,4),
                   (4,5),
                   (5,6),
                   (6,7),
                   (7,8),
                   (8,9),
                   (9,10), ]
        result = self.target(load,run)
        self.assertEqual(expect,result)

    def test_several_pages_removed(self):
        load = "python loaddb.py data/test/A.pdf data/test/C.pdf"
        run = "python inspection.py"
        expect = [ (1,1),
                   (2,2),
                   (4,3),
                   (5,4),
                   (7,5),
                   (8,6),
                   (9,7), 
                          ]
        result = self.target(load,run)
        self.assertEqual(expect,result)

        load = "python loaddb.py data/test/C.pdf data/test/A.pdf"
        run = "python inspection.py"
        expect = [ (1,1),
                   (2,2),
                   (3,4),
                   (4,5),
                   (5,7),
                   (6,8),
                   (7,9), 
                          ]
        result = self.target(load,run)
        self.assertEqual(expect,result)


    def test_image_shift(self):
        load = "python loaddb.py data/test/A.pdf data/test/D.pdf"
        run = "python inspection.py"
        expect = [ (1,1),
                   (3,3),
                   (9,9),
                   (10,10), 
                          ]
        result = self.target(load,run)
        self.assertEqual(expect,result)

        load = "python loaddb.py data/test/A.pdf data/test/D.pdf"
        run = "python inspection.py --include MyTest1 --check any"
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
        result = self.target(load,run)
        self.assertEqual(expect,result)

if __name__ == '__main__':
    unittest.main()

