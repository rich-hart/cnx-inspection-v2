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

if __name__ == '__main__':
    unittest.main()


