import unittest
import array as arr
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value=36)
    def test_search_array_item_found(self, mock_input):
        self.assertEqual(3, sort_and_search_array.search_array([1, 4, 5, 36, 99]))

    @patch('builtins.input', return_value=100)
    def test_search_array_item_not_found(self, mock_input):
        self.assertEqual(-1, sort_and_search_array.search_array([1, 4, 5, 36, 99]))

    def test_sort_array(self):
        unsorted_list = [99, 1, 4, 5, 36]
        sorted_list = [1, 4, 5, 36, 99]
        self.assertEqual(sorted_list, sort_and_search_array.sort_array(unsorted_list))


if __name__ == '__main__':
    unittest.main()
