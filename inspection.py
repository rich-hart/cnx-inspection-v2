import unittest
import argparse
import logging


from utils import test_generator

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
    parser.add_argument('--cases', type=str, default='cases.py')

    args = parser.parse_args(argv)

    settings = vars(args)

    load_tests = test_generator(settings)

    logging.basicConfig(filename=settings['results'])

    with open(settings['output'],'w') as f:
        test_output = unittest.TextTestRunner(f,verbosity=3)
        unittest.main(testRunner=test_output)

if __name__ == "__main__":
    main() 
