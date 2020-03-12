from Statistics.Statistics import Statistics
from PopulationSampling.SimpleRandom import simpleRandomSample

class PopulationSampling(Statistics):

    def __init__(self):
        super().__init__()

    def simpleRandomSample(self, population, numSelect):
        self.result = simpleRandomSample(population, numSelect)
        return self.result