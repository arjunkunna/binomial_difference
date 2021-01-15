from scipy.stats import binom
from scipy.stats import beta
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import math


#set true values of a and b
a = 0.9
b = 0.5
q = a-b

beta = [0.5, 0.75, 0.9, 0.95, 0.99]
n1 = [1, 10, 100, 1000, 10000, 100000]
n2 = [1, 10, 100, 1000, 10000, 100000]
n = n1
sample_size = 500

#generate data
for n_iter in n1:
    data_x = binom.rvs(n_iter, a, size=sample_size)
    data_y = binom.rvs(n_iter, b, size=sample_size)

    #compute our estimate
    a_hat = data_x/n_iter
    b_hat = data_y/n_iter
    q_hat = a_hat - b_hat
    mse = np.sum(pow(q_hat-q, 2))
    print("N = ", n_iter, "; MSE = ", mse)


    #compute our confidence interval
    for beta_iter in beta:
        alpha = 1 - beta_iter
        lower_quantile = alpha/2
        upper_quantile = 1-(lower_quantile)

        z_score = norm.ppf(upper_quantile)

        in_interval = 0

        for i in range(sample_size):
            coef = z_score*math.sqrt((a_hat[i]*(1-a_hat[i]) + b_hat[i]*(1-b_hat[i])) / n_iter)
            conf_int = (q_hat[i] - coef, q_hat[i] + coef)

            if ((q > conf_int[0]) and (q < conf_int[1])) :
                in_interval += 1

        print("N = ", n_iter, "; beta = ", beta_iter, "; coverage = ", in_interval/sample_size)
        print("Sample interval = ", conf_int, "\n")




        #print("Q_hat is ", q_hat, " and confidence interval is ", conf_int)
