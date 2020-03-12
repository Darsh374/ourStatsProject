import unittest
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:

        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean([2, 4, 6, 8, 10])
        self.assertEqual(mean, 6)

    def test_median_calculator(self):
        median = self.statistics.median([2, 4, 6, 8, 10])
        self.assertEqual(median, 6)