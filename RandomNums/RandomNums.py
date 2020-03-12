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

        # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def RangeNums(self):
        random.seed(50)
        randomNumbers = []
        n = sum(randomNumbers)
        i = 0
        while i < n:
            randomNumbers.append(random.randint(1, 100))
            i += 1
            pprint.pprint(randomNumbers)


#Select a random item from a list
    def RandomItem(self):
        numberList = [134535, 5456464, 35435, 5646, 1212]
        randomChoice = random.choice(numberList)
        return randomChoice