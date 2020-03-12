import unittest
from PopulationSampling.PopulationSampling import PopulationSampling
import random
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.PopulationSampling = PopulationSampling()
        self.testData = []
        random.seed(5)
        i = 0
        while i < 11:
            self.testData.append(random.randint(1, 50))
            i += 1

        self.big_testData = []
        random.seed(6)
        i = 0
        while i < 100:
            self.big_testData.append(random.randint(1, 100))
            i += 1

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.PopulationSampling, PopulationSampling)

    def test_simplerandom_statistics(self):
        simpleRandomSample = self.PopulationSampling.simpleRandomSample(self.testData, 3)
        self.assertEqual(simpleRandomSample, [34, 40, 23])

        # test systematic sampling

    def test_systematicsampling_statistics(self):
        systematicSample = self.PopulationSampling.systematicSampling(self.big_testData, 10)
        self.assertEqual(systematicSample, [])
        