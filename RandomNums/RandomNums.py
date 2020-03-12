import random
import pprint

class RandomNums:
    def __init__(self):
        self.RandomNums = None

#Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def RandIntNoSeed(self):
        self.randomInteger = random.randint(1,50)
        return self.randomInteger

    def RandDecNoSeed(self):
        self.randomDecimal = random.random()
        return self.randomDecimal