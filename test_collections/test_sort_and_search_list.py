import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value=36)
    def test_search_list_item_found(self, mock_input):
        self.assertEqual(3, sort_and_search_list.search_list([1, 4, 5, 36, 99]))

    @patch('builtins.input', return_value=100)
    def test_search_list_item_not_found(self, mock_input):
        self.assertEqual(-1, sort_and_search_list.search_list([1, 4, 5, 36, 99]))

    def test_sort_list(self):
        unsorted_list = [99, 1, 4, 5, 36]
        sorted_list = [1, 4, 5, 36, 99]
        self.assertEqual(sorted_list, sort_and_search_list.sort_list(unsorted_list))


if __name__ == '__main__':
    unittest.main()
