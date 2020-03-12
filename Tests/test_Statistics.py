import unittest
import random
import pprint
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(5)
        self.randomData = []
        i = 0
        while i < 6:
            self.randomData.append(random.randint(1, 100))
            i += 1
        #pprint.pprint(self.randomData)
        #[80, 33, 95, 46, 89, 95]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean([2, 4, 6, 8, 10])
        self.assertEqual(mean, 6)

    def test_median_calculator(self):
        median = self.statistics.median([2, 4, 6, 8, 10])
        self.assertEqual(median, 6)

    def test_mode_calculator(self):
        mode = self.statistics.mode([22, 33, 44, 44, 53])
        self.assertEqual(mode, [44])

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.randomData)
        self.assertEqual(variance, 2235.5)

    def test_standard_deviation_calculator(self):
        standard_deviation = self.statistics.standard_deviation(self.randomData)
        self.assertEqual(standard_deviation, 47.281074437876306)

    def test_quartliles_statistics(self):
        quartiles = self.statistics.quartile(self.randomData)
        self.assertEqual(quartiles, (54.5, 84.5, 93.5))

    def test_skewness_statisitcs(self):
        skewness = self.statistics.skewness(self.randomData)
        self.assertEqual(skewness, -0.4653024547677381)

if __name__ == '__main__':
    unittest.main()