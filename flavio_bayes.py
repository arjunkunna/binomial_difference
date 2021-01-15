from scipy.stats import binom
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import math


#set true values of a and b
a = 0.6
b = 0.62

n1 = 10000
n2 = 10000

#generate data
data_x = binom.rvs(n1, a, 1)
data_y = binom.rvs(n2, b, 1)

beta_a_1 = data_x + 1
beta_a_2 = data_y + 1

beta_b_1 = n1 - data_x + 1
beta_b_2 = n2 - data_y + 1


q_sim = beta.rvs(beta_a_1, beta_b_1, size=10000) - beta.rvs(beta_a_2, beta_b_2, size=10000)

plt.hist(q_sim, bins = 50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
#plt.show()
print(q_sim)

beta = 0.98
alpha = 1-beta
lower_quantile = alpha/2
upper_quantile = 1-(lower_quantile)

credible_interval = (np.quantile(q_sim, lower_quantile), np.quantile(q_sim, upper_quantile))
print(credible_interval)
