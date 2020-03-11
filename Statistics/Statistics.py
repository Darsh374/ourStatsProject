from Calculator.calculator import Calculator
from Statistics.Mean import mean


class Statistics(Calculator):

    def __init__(self):
        super().__init__()
        self.data = None

    def mean(self, data):
        self.result = mean()
        return self.result
