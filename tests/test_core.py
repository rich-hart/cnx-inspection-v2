import sys
import os
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

import unittest
import psycopg2
import subprocess
import loaddb


DATABASE='png-testing'
USER='qa'
PDF_A = os.path.join(os.getcwd(),'tests/data/A.pdf')
PDF_B = os.path.join(os.getcwd(),'tests/data/B.pdf')

class LOADDB(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         with psycopg2.connect(database='png-testing') as con:
             with con.cursor() as cur:
                 cur.execute("CREATE TABLE test_a_png (Id INT PRIMARY KEY, Data BYTEA)")
                 cur.execute("CREATE TABLE test_b_png (Id INT PRIMARY KEY, Data BYTEA)")

     def test_loading_db(self):
         
         command = "--database {0} {1} {2}".format(DATABASE,PDF_A,PDF_B)
         loaddb.main(command.split())

     @classmethod
     def tearDownClass(cls):
         with psycopg2.connect(database='png-testing') as con:
             with con.cursor() as cur:
                 cur.execute("DROP TABLE test_a_png")
                 cur.execute("DROP TABLE test_b_png")

RESULT_LOG = os.path.join(os.getcwd(),'tests/data/results.log')
class Utils(unittest.TestCase):
     def test_load_result_log(self):
         from utils import load_result_log
         import ipdb; ipdb.set_trace()
         results_list = load_result_log(RESULT_LOG)
         for result in results_list:
             self.assertIsInstance(result,dict)
             keys_list=[key for key, value in result.iteritems()] 
             self.assertIn('case',keys_list)
             self.assertIn('page_i',keys_list)
             self.assertIn('page_j',keys_list)
             self.assertIn('test',keys_list)
             self.assertIn('result',keys_list)
if __name__ == '__main__':
    unittest.main()


