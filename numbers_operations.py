import numpy as np
class NumbersOperations:

    def generate_set(self, mu, sigma, n):
        return np.random.normal(mu, sigma, n)

    def get_frequencies_in_set(self, set):
        _, counts = np.unique(set, return_counts=True)
        return counts

    def get_unique(self, set):
        return np.unique(set)

    def get_selective_dispersion(self, set):
        selective_dispersion = 0