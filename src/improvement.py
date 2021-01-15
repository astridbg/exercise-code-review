import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

num_measurements = 25

# read data from file
data = pd.read_csv('data/temperatures.csv', nrows=num_measurements)
temperatures = data['Air temperature (degC)']

# compute statistics
mean = np.mean(temperatures)

# plot results
plt.plot(temperatures, 'r-')
plt.axhline(y=mean, color='b', linestyle='--')
plt.savefig('25.png')
plt.clf()
