import get_column_stats
import unittest
import os
import random
import statistics

test_array = [1, 2, 3, 4, 5]
test_array_std = 1.4142135623730951


class TestGet_Column_Stats(unittest.TestCase):

    def setUp(self):
        self.test_array = [1, 2, 3, 4, 5]
        self.test_array_std = 1.4142135623730951
        self.direct_mean_list = []
        self.file_mean_list = []
        for i in range(100):
            rand_int = random.randint(1, 100)
            self.direct_mean_list.append(rand_int)
            self.file_mean_list.append(rand_int)

        self.direct_mean_val = statistics.mean(self.direct_mean_list)

    def test_direct_mean(self):
        file_mean = get_column_stats.mean(self.file_mean_list)
        self.assertEqual(file_mean, self.direct_mean_val)

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            get_column_stats.mean([])

    def test_std_empty(self):
        with self.assertRaises(ValueError):
            get_column_stats.stdev([])

    def test_std_one_element(self):
        with self.assertRaises(ValueError):
            get_column_stats.stdev([random.randint(1, 1000)])

    def test_mean_constant(self):
        self.assertEqual(get_column_stats.mean(self.test_array), 3)

    def test_stdev_constant(self):
        self.assertEqual(get_column_stats.stdev(test_array),
                         self.test_array_std)


if __name__ == '__main__':
    unittest.main()
