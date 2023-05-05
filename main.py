from numbers_operations import NumbersOperations
from diagrams import Diagrams

diagrams = Diagrams()
numbers_operations = NumbersOperations()

# COLORS
C_RED = '\033[91m'
C_YELLOW = '\033[93m'
C_END = '\033[0m'

# 32
variant = 120 % 11 + 11 * 2
print(f'{C_RED}Variant:{C_END} {variant}')

# GENERATING SET
n = 134
mu = 0
sigma = 1.7

set = numbers_operations.generate_set(mu, sigma, n)
set = [round(x, 0) for x in set]
counts = numbers_operations.get_frequencies_in_set(set)
uniques = numbers_operations.get_unique(set)
print(set)

# STATISTICS

print(f'{C_YELLOW}Середнє арифметичне:{C_END} {str(numbers_operations.get_selective_average(set))}')
print(f"{C_YELLOW}Вибіркова дисперсія:{C_END} {numbers_operations.get_selective_dispersion(set)}")
print(f"{C_YELLOW}Вибіркове стандартне відхилення:{C_END} {numbers_operations.get_selective_standard_deviation(set)}")
print(f"{C_YELLOW}Медіана:{C_END} {str(numbers_operations.get_median(set))}" )
print(f"{C_YELLOW}Мода:{C_END} {str(numbers_operations.get_moda(set))}")

# POLYGON
diagrams.generate_polygon(uniques, counts)
diagrams.show_diagram()

# HISTOGRAM
diagrams.generate_histogram(set)
diagrams.show_diagram()

# BOX PLOT
diagrams.generate_boxplot(set)
diagrams.show_diagram()

# PIE PLOT
diagrams.generate_pie(counts, uniques)
diagrams.show_diagram()

# PARETO PLOT
diagrams.generate_pareto(uniques, counts)
diagrams.show_diagram()


