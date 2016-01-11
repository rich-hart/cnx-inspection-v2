import unittest
from cases import DefaultTest
from importlib import import_module
import psycopg2
import inspect
def test_generator(settings):
    test_cases = unittest.TestSuite()
    cases = import_module(settings['cases'])

    with psycopg2.connect(database=settings['database']) as con:
        with con.cursor() as cur:
            cur.execute("SELECT COUNT(Page) FROM png_a")
            total_M= cur.fetchone()[0]
            cur.execute("SELECT COUNT(Page) FROM png_b")
            total_N= cur.fetchone()[0] 
    for case_name in settings['include']:
        TestClass = cases.__getattribute__(case_name)
        setattr(TestClass,'_settings',settings)
        SuperClass = inspect.getmro(TestClass)[1]

        method_list = inspect.getmembers(TestClass, predicate=inspect.ismethod)
        super_method_list = inspect.getmembers(SuperClass,predicate=inspect.ismethod)
        test_method_list = list(set(method_list)-set(super_method_list))
        test_name_list = [ method[0] for method in test_method_list if method[0]!='tearDownClass' and method[0]!='setUpClass']
        for test_name in test_name_list:
            for pi in range(0,total_M):
                for pj in range(0,total_N):
                    test_cases.addTest(TestClass(test_name, pi, pj))
    def load_tests(loader, tests, pattern):
    # FIXME: declare me as a decorator
        return test_cases

    return load_tests

def load_result_log(filepath):
    results = []
    with open(filepath,'r') as f:
        for line in f:
            info = eval(line)
            results.append(info)
    return results


