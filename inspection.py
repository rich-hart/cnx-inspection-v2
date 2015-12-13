import unittest
import argparse

from utils import test_generator

load_tests = None

def main(argv=None):
    global load_tests

#    from utils import load_png_tests
#    load_tests = load_png_tests


    parser = argparse.ArgumentParser()

    parser.add_argument('--include', action='append', default=['DefaultTest'])

    parser.add_argument('--exclude', action='append', default=None)

    args = parser.parse_args(argv)

    settings = vars(args)

    load_tests= test_generator(settings)
#    settings['test_cases'] = set(settings['include'])-set(settings['exclude'])
 
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main() 
