import unittest
from List_Filtering import filter_list


class MyTestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1,2])  # add assertion here


if __name__ == '__main__':
    unittest.main()
