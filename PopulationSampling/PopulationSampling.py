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

    def margin_error(self, data, sample_size):
        self.result = margin_error(data, sample_size)
        return self.result

    def sample_size(self, data, proportion):
        self.result = sampleSize(data, proportion)
        return self.result

    def sample_size_unknown(self, percent, confidence, width):
        self.result = sample_size_unknown(percent, confidence, width)
        return self.result

    def samplesizeKnownPop(self, data, confidence, error):
        self.result = samplesizeKnownPop(data, confidence, error)
        return self.result


