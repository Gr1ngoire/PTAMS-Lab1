import matplotlib.pyplot as plt
class Diagrams:
    def __init__(self):
        self.plt = plt

    def generate_polygon(self, x, y):
        self.plt.plot(x, y)

    def generate_histogram(self, x):
        self.plt.hist(x)

    def generate_boxplot(self, x):
        self.plt.boxplot(x)

    def show_diagram(self):
        self.plt.show()