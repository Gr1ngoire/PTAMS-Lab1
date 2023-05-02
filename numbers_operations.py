import numpy as np
class NumbersOperations:

    def generate_set(self, mu, sigma, n):
        return np.random.normal(mu, sigma, n)

    def get_frequencies_in_set(self, set):
        _, counts = np.unique(set, return_counts=True)
        return counts

    def get_selective_average(self, set):
        counter = 0
        for i in range(len(set)):
            counter += set[i]
        return counter / len(set)

    def get_unique(self, set):
        return np.unique(set)

    def get_selective_dispersion(self, set):
        n = len(set)
        selective_dispersion = 0

    def get_moda(self, set):
        index = 0
        value = 0
        freq_set = self.get_frequencies_in_set(set)
        for i in range(len(freq_set)):
            if freq_set[i] > value:
                value = freq_set[i]
                index = i
        return set[index]

        average = self.get_selective_average(set)
        for x in set:
            selective_dispersion += (x - average)**2
        return selective_dispersion / (n - 1)

    def get_selective_standard_deviation(self, set):
        dispersion = self.get_selective_dispersion(set)
        return pow(dispersion, 0.5)