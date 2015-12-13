import unittest
import argparse

from utils import test_generator

load_tests = None

def main(argv=None):
    global load_tests

    parser = argparse.ArgumentParser()

    parser.add_argument('--include', action='append', default=['DefaultTest'])

    parser.add_argument('--exclude', action='append', default=None)

    args = parser.parse_args(argv)

    settings = vars(args)

    load_tests= test_generator(settings)
    with open('output.log','w') as f:
        test_output = unittest.TextTestRunner(f,verbosity=3)
        unittest.main(testRunner=test_output)

if __name__ == "__main__":
    main() 
