import unittest
from numpy.random import seed
from numpy.random import randint
import random
from RandomNums.RandomNums import RandomNums
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.randomNums = RandomNums()
        self.testData = []
        random.seed(10)
        i = 0
        while i < 11:
            self.testData.append(random.randint(1, 100))
            i += 1
        #pprint.pprint(self.testData)

    def test_instantiate_random(self):
        self.assertIsInstance(self.randomNums, RandomNums)

    def test_noseedINT_random(self):
        noseedInt = self.randomNums.RandIntNoSeed()
        #self.assertEqual(noseedInt, 42)
        pprint.pprint(noseedInt)

    def test_noseedDEC_random(self):
        noseedDec = self.randomNums.RandDecNoSeed()
        #self.assertEqual(noseedDec, .4557)
        pprint.pprint(noseedDec)
