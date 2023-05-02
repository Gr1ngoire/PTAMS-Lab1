import numpy as np


class NumbersOperations:

    def generate_set(self, mu, sigma, n):
        return np.random.normal(mu, sigma, n)

    def get_frequencies_in_set(self, set):
        _, counts = np.unique(set, return_counts=True)
        return counts

    def get_sample_average(self, set):
        counter = 0
        for i in range(len(set)):
            counter += set[i]
        return counter / len(set)