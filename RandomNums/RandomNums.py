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

        # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def RandIntSeed(self):
        random.seed(3)
        self.randomInt = random.randint(1, 50)
        return self.randomInt

    def RandDecSeed(self):
        random.seed(3)
        self.randomDec = random.random()
        return self.randomDec
