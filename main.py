from numbers_operations import NumbersOperations
from diagrams import Diagrams

diagrams = Diagrams()
numbers_operations = NumbersOperations()

# 32
variant = 120 % 11 + 11 * 2
print(variant)

# GENERATING SET
n = 134
mu = 0
sigma = 1.7

set = numbers_operations.generate_set(mu, sigma, n)
set = [round(x, 2) for x in set]
counts = numbers_operations.get_frequencies_in_set(set)
set = numbers_operations.get_unique(set)
print(set, counts)


# POLYGON
diagrams.generate_polygon(set, counts)
diagrams.show_diagram()

# HISTOGRAM
diagrams.generate_histogram(set)
diagrams.show_diagram()

print("Середнє арифметичне: " + str(numbers_operations.get_sample_average(set)))