import numpy as np
import matplotlib.pyplot as plt

# 32
variant = 120 % 11 + 11 * 2
print(variant)

# GENERATING SET
n = 134
mu = 0
sigma = 1.7

set = np.random.normal(mu, sigma, n)
_, counts = np.unique(set, return_counts=True)
print(set, counts)

# POLYGON
plt.plot(set, counts)
plt.show()

# HISTOGRAM
plt.hist(set)
plt.show()