import unittest
import argparse
import logging
from multiprocessing import Process

from utils import generate_tests, lcs_images

load_tests = None

def run(settings):
    global load_tests
    load_tests = generate_tests(settings)
    with open(settings['output'],'w+') as f:
        output = unittest.TextTestRunner(f,verbosity=3)
        unittest.main(testRunner=output,argv=['inspection.py'])

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--include', action='append', default=['DefaultTest'], help="Include additional test classes (default=[DefaultTest])")
    parser.add_argument('--exclude', action='append', default=[], help="Exclude test classes.")
    parser.add_argument('--output', type=str, default='output.log', help="Test execution output file (default=output.log).")
    parser.add_argument('--results', type=str, default='results.log', help="Test results output file, each line is a python dictionary (default=results.log).")
    parser.add_argument('--cases', type=str, default='cases', help="Python module which stores test cases (default=cases).")
    parser.add_argument('--check', type=str, choices=['any','all'],default='all', help="Require that any/all test cases pass for pages to be related (default=all).")
    parser.add_argument('pdf_a', type=str)
    parser.add_argument('pdf_b', type=str) 

    args = parser.parse_args(argv)
    
    settings = vars(args)

    logging.basicConfig(filename=settings['results'],level=logging.INFO,filemode='w+', format='')

    p = Process(target=run,args=(settings,))

    p.start()
    p.join()

    print lcs_images(settings['results'],settings['check'])

if __name__ == "__main__":
    main() 
