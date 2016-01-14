import unittest
import argparse
import logging

from utils import test_generator, lcs_images

load_tests = None

def main(argv=None):
    global load_tests

    parser = argparse.ArgumentParser()

    # FIXME: use nargs='+' for lists
    parser.add_argument('--include', action='append', default=['DefaultTest'])
    parser.add_argument('--exclude', action='append', default=None)
    parser.add_argument('--output', type=str, default='output.log')
    parser.add_argument('--results', type=str, default='results.log')
    parser.add_argument('--database', type=str, default='png-testing')
    parser.add_argument('--user', type=str, default='qa')
    parser.add_argument('--cases', type=str, default='cases')
    # FIXME: add any / all argument
    # FIXME: add single test and page numbers needed. 
    args = parser.parse_args(argv)
    
    settings = vars(args)
    
    load_tests = test_generator(settings)

    logging.basicConfig(filename=settings['results'],level=logging.INFO,filemode='w+', format='')

    # FIXME: Will need the multiprocessing library so unittests can run with 
    # other tasks

    with open(settings['output'],'w+') as f:
        test_output = unittest.TextTestRunner(f,verbosity=3)
        unittest.main(testRunner=test_output,argv=['inspection.py'])
#    with open("lsc.txt",'w+') as f:
#        f.write(str(lcs_images(settings['results'])))

if __name__ == "__main__":
    main() 
