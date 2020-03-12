from Statistics.Statistics import Statistics
from PopulationSampling.SimpleRandom import simpleRandomSample
from PopulationSampling.SystematicSampling import systematicSampling


class PopulationSampling(Statistics):

    def __init__(self):
        super().__init__()

    def simpleRandomSample(self, population, numSelect):
        self.result = simpleRandomSample(population, numSelect)
        return self.result

    def systematicSampling(self, data, sample_size):
        self.result = systematicSampling(data, sample_size)
        return self.result
    def confidenceInterval(self, data):
        self.result = confidenceInterval(data)
        return self.result