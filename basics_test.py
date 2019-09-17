import get_column_stats
import unittest

tArray = [1,2,3,4,5]

class TestGet_Column_Stats(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(get_column_stats.mean(tArray), 3)

    def test_stdev(self):
        self.assertEqual(get_column_stats.stdev(tArray), 1.4142135623730951)

if __name__ == '__main__':
    unittest.main()