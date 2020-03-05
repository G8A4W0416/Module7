import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-1')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()


if __name__ == '__main__':
    unittest.main()
