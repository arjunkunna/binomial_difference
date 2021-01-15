from scipy.stats import binom
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import math


#set true values of a and b
a = 0.9
b = 0.5
q = a-b

beta_arr = [0.5, 0.75, 0.9, 0.95, 0.99]
n1 = [1, 10, 100, 1000, 10000, 100000]
n2 = [100, 1000, 10000, 100000, 1000000, 10000000]
sample_size = 500

#generate data
for k in range(len(n2)):
    for i in range(len(n1)):
        data_x = binom.rvs(n1[i], a, size=sample_size)
        data_y = binom.rvs(n2[k], b, size=sample_size)

        beta_a_1 = data_x + 1
        beta_a_2 = data_y + 1

        beta_b_1 = n1[i] - data_x + 1
        beta_b_2 = n2[k] - data_y + 1


        for beta_iter in beta_arr:
            alpha = 1 - beta_iter
            lower_quantile = alpha/2
            upper_quantile = 1-(lower_quantile)

            in_interval = 0
            for j in range(sample_size):
                q_sim = beta.rvs(beta_a_1[j], beta_b_1[j], size=10000) - beta.rvs(beta_a_2[j], beta_b_2[j], size=10000)
                #plt.hist(q_sim, bins = 50)
                #plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
                #plt.show()
                credible_interval = (np.quantile(q_sim, lower_quantile), np.quantile(q_sim, upper_quantile))
                if ((q > credible_interval[0]) and (q < credible_interval[1])) :
                    in_interval += 1


        print("n1 = ", n1[i], "n2 = ", n2[k], "; beta = ", beta_iter, "; coverage = ", in_interval/sample_size)
        print("Sample interval = ", credible_interval, "\n")
