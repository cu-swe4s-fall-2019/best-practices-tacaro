import get_column_stats
import unittest
import os
import random

test_array = [1, 2, 3, 4, 5]
test_array_std = 1.4142135623730951

class TestGet_Column_Stats(unittest.TestCase):
    def setUp(self):
        test_array = [1, 2, 3, 4, 5]
        test_array_std = 1.4142135623730951
        self.test_file_name = 'generic_name.txt'
        f = open(self.test_file_name, 'w') # what does the W do?

        

    def test_mean_constant(self):
        self.assertEqual(get_column_stats.mean(test_array), 3)

    def test_stdev_constant(self):
        self.assertEqual(get_column_stats.stdev(test_array), test_array_std)


if __name__ == '__main__':
    unittest.main()
