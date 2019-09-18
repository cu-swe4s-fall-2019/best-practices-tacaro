import get_column_stats
import unittest
import os
import random

test_array = [1, 2, 3, 4, 5]
test_array_std = 1.4142135623730951

class TestGet_Column_Stats(unittest.TestCase):
    def setUp(self):
        self.test_array = [1, 2, 3, 4, 5]
        self.test_array_std = 1.4142135623730951

        self.direct_sum = []
        self.direct_mean = 0

        self.test_file_name = 'generic_name.txt'
        f = open(self.test_file_name, 'w') # what does the W do?

        ''' THIS PART IS NOT WORKING CURRENTLY
        for i in range(100):
            rand_int = random.randint(1,100)
            f.write(str(rand_int) + '\n')
        
        for i in f:
            self.direct_sum.append(i)
            self.direct_mean = self.direct_sum/len(f)

        f.close()
        '''

    def tearDown(self):
        os.remove(self.test_file_name)

    ''' THIS PART IS NOT WORKING CURRENTLY
    def test_file_mean_rand(self):
        file_mean = get_column_stats.mean(self.test_file_name)
        self.assertEqual(file_mean, self.direct_mean)
    '''

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            get_column_stats.mean([])

    def test_std_empty(self):
        with self.assertRaises(ValueError):
            get_column_stats.stdev([])

    def test_std_one_element(self):  # what will stdev do with a single-element array?
        with self.assertRaises(ValueError):
            get_column_stats.stdev([random.randint(1,1000)])

    def test_mean_string(self):
        with self.assertRaises(ValueError):
            get_column_stats.mean([1,2,3,"a"])

    def test_mean_constant(self):
        self.assertEqual(get_column_stats.mean(self.test_array), 3)

    def test_stdev_constant(self):
        self.assertEqual(get_column_stats.stdev(test_array), self.test_array_std)


if __name__ == '__main__':
    unittest.main()
