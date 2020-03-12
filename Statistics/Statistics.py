from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median

class Statistics(Calculator):

    def __init__(self):
        super().__init__()
        self.data = None

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result
    