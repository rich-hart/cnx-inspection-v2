import unittest
from cases import DefaultTest
from importlib import import_module
import psycopg2
import inspect
import numpy

def test_generator(settings):
    test_cases = unittest.TestSuite()
    cases = import_module(settings['cases'])

    with psycopg2.connect(database=settings['database']) as con:
        with con.cursor() as cur:
            cur.execute("SELECT Page FROM png_a")
            pages_a = cur.fetchall()
            pages_a = [ page[0] for page in pages_a]
            cur.execute("SELECT Page FROM png_b")
            pages_b = cur.fetchall() 
            pages_b = [ page[0] for page in pages_b]
    for case_name in settings['include']:
        TestClass = cases.__getattribute__(case_name)
        setattr(TestClass,'_settings',settings)
        SuperClass = inspect.getmro(TestClass)[1]

        method_list = inspect.getmembers(TestClass, predicate=inspect.ismethod)
        super_method_list = inspect.getmembers(SuperClass,predicate=inspect.ismethod)
        test_method_list = list(set(method_list)-set(super_method_list))
        test_name_list = [ method[0] for method in test_method_list if method[0]!='tearDownClass' and method[0]!='setUpClass']
        for test_name in test_name_list:
            for pi in pages_a:
                for pj in pages_b:
                    test_cases.addTest(TestClass(test_name, pi, pj))
    def load_tests(loader, tests, pattern):
    # FIXME: declare me as a decorator
        return test_cases

    return load_tests


# FIXME: These utility functions will need to be corrected base on the nature of 
# translating the lcs problem from strings to images



def load_result_log(filepath):
    results = []
    with open(filepath,'r') as f:
        for line in f:
            info = eval(line)
            results.append(info)
    return results

def generate_info_matrix(info_list):
    test_cases = set([(info['test'],info['case']) for info in info_list])
    pages_a = set([info['page_i'] for info in info_list])
    pages_b = set([info['page_j'] for info in info_list])

    test_cases = list(test_cases)
    pages_a = list(pages_a)
    pages_b = list(pages_b)

    info_matrix = numpy.chararray((len(test_cases),
                                  len(pages_a)+1,
                                  len(pages_b)+1))

    info_matrix[:] = 'f'

    for info in info_list:
        x = test_cases.index((info['test'],info['case']))
        y = info['page_i']
        z = info['page_j']

        value = info['result']
        info_matrix[x,y,z] = value

    return info_matrix

def generate_comp_matrix(info_matrix,operation,skipped_results=True):

    (A,B,C) = info_matrix.shape

    comp_matrix = numpy.zeros((B,C), dtype=bool)

    value_matrix = numpy.zeros(info_matrix.shape, dtype=bool)

    for a in range(0,A):
        for b in range(0,B):
            for c in range(0,C):
                info = info_matrix[a,b,c]
                if info == 'p':
                    value = True
                elif info == 'f':
                    value = False
                elif info == 'e':
                    value = False
                elif info == 's':
                    value = skipped_results
                else:
                    value = False
                value_matrix[a,b,c]=value

    if not isinstance(operation,str):
        raise TypeError
    if operation.lower() == 'all':
        numpy.all(value_matrix,axis=0,out=comp_matrix)
    elif operation.lower() == 'any':
        numpy.any(value_matrix,axis=0,out=comp_matrix)
    else:
        raise ValueError("operation must be 'all' or 'any'")

    return comp_matrix

def LCSLength(comp_matrix):
    (M,N) = comp_matrix.shape
    length_matrix = numpy.zeros((M,N), dtype=int)

    for i in range(1,M):
        for j in range(1,N):
            if comp_matrix[i,j]:
                length_matrix[i,j] = length_matrix[i-1,j-1] + 1
            else:
                length_matrix[i,j] = max(length_matrix[i,j-1],length_matrix[i-1,j])
    return length_matrix

def backtrack(length_matrix,comp_matrix,i,j):
    if i == 0 or j == 0:
        return []
    elif comp_matrix[i,j]:
        return backtrack(length_matrix,comp_matrix,i-1,j-1)+[i]
    else:
        if length_matrix[i,j-1]>length_matrix[i-1,j]:
            return backtrack(length_matrix,comp_matrix,i,j-1)
        else:
            return backtrack(length_matrix,comp_matrix,i-1,j)


def printDiff(length_matrix,comp_matrix,i,j):
    if i > 0 and j > 0 and comp_matrix[i,j]:
        printDiff(length_matrix,comp_matrix,i-1,j-1)
        print("  " + str(i))
    elif j > 0 and (i == 0 or length_matrix[i,j-1] >= length_matrix[i-1,j]):
        printDiff(length_matrix,comp_matrix,i, j-1)
        print("+ " + str(j))
    elif i > 0 and (j == 0 or length_matrix[i,j-1] < length_matrix[i-1,j]):
        printDiff(length_matrix,comp_matrix, i-1,j)
        print("- " + str(i))
    else:
        print("")


def lcs_images(results_file_path,require='ANY'):
    results_list=load_result_log(results_file_path)
    info_matrix = generate_info_matrix(results_list)
    comp_matrix = generate_comp_matrix(info_matrix,require)
    length_matrix = LCSLength(comp_matrix)
    (M,N) = length_matrix.shape
    lcs = backtrack(length_matrix,comp_matrix,M-1,N-1)
    return lcs
