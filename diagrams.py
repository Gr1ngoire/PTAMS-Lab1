import matplotlib.pyplot as plt
import numpy as np

class Diagrams:
    def __init__(self):
        self.plt = plt

    def generate_polygon(self, x, y):
        self.plt.plot(x, y)

    def generate_histogram(self, x):
        n = len(np.unique(x))
        self.plt.hist(x, bins=n, edgecolor='black')

    def generate_boxplot(self, x):
        self.plt.boxplot(x)

    def generate_pie(self, x, y):
        self.plt.rcParams['font.size'] = 8.0
        self.plt.pie(x, labels=y)

    def generate_pareto(self, x, y):
        pairs = list(zip(x, y))
        pairs.sort(key=lambda pair: pair[1], reverse=True)
        x, y = zip(*pairs)
        x = [str(i) for i in x]
        self.plt.bar(x, y)
        
        cumsum = np.cumsum(y)
        relative_cumsum = cumsum / cumsum[-1]

        self.plt.twinx().plot(x, relative_cumsum, color='red', marker='o')
        # put relative cumsum values on plot dots
        for i in range(len(x)):
            self.plt.text(x[i], relative_cumsum[i], str(round(relative_cumsum[i], 2)))


    def show_diagram(self):
        self.plt.show()