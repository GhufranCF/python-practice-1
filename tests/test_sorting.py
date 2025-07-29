import unittest
from sort_dictionaries import sort_dictionaries

class SortingTest(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            {'name': 'Charlie', 'age' : 21},
            {'name': 'Bob', 'age' : 20},
            {'name': 'Alice', 'age' : 22,}]
    def test_sort_numeric_key(self):
        result = sort_dictionaries(self.test_case, 'age')
        expected = [
            {'name': 'Bob', 'age' : 20,},
            {'name': 'Charlie', 'age' : 21,},
            {'name': 'Alice', 'age' : 22,}]
        self.assertEqual(result, expected)


    def test_string_key(self):
        result = sort_dictionaries(self.test_case, 'name')
        expected = [
            {'name': 'Alice', 'age' : 22,},
            {'name': 'Bob', 'age' : 20,},
            {'name': 'Charlie', 'age' : 21,},
        ]

        self.assertEqual(result, expected)


    def test_non_existing_key(self):
        with self.assertRaises(KeyError):
            result = sort_dictionaries(self.test_case, 'no_key')
