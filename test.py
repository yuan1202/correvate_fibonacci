import os
import itertools
import unittest
from utils import load_input, write_output, get_fib


class Tests(unittest.TestCase):

    def test_load_0(self):
        print('\nLoad test #0: raise exception when input file has wrong format')
        with self.assertRaises(Exception):
            load_input('./input/test0.csv')

    def test_load_1(self):
        print('\nLoad test #1: check if negative values are forced to be 0')
        _, data = load_input('./input/test1.csv')
        self.assertEqual(min(itertools.chain(*data)), 0)

    def test_fibonacci(self):
        print('\nFibonacci test: check if fibonacci calculation is correct')
        correct = {i: v for i, v in enumerate([0,1,1,2,3,5,8,13,21,34,55,89])}
        results = get_fib(list(range(12)))
        self.assertEqual(correct, results)

    def test_write(self):
        print('\nWrite test: check if writing function works')
        header = ['Col1', 'Col2', 'Col3']
        data = [[1, 2, 3], [4, 5, 6]]
        write_output('./test_output.csv', header, data)
        self.assertTrue(os.path.exists('./test_output.csv'))
        _, reloaded_data = load_input('./test_output.csv')
        self.assertEqual(data, reloaded_data)
        os.remove('./test_output.csv')

if __name__ == '__main__':
    unittest.main()