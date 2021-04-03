import numpy as np

# Perceptron Algorithm Passing Through the Origin

def perceptron_origin(x,y,T):
    theta = np.array([0, 0])
    for run in range(T):
        for i in range(x.shape[0]):
            if y[i]*theta.dot(x[i]) <= 0:
                theta = theta+ y[i]*x[i]
            else:
                pass
    return theta

# General Perceptron Algorithm
def perceptron_full(x,y,T):
    theta = np.array([0, 0])
    theta_0 = 0
    for run in range(T):
        for i in range(x.shape[0]):
            if y[i]*(theta.dot(x[i]) + theta_0) <= 0:
                theta = theta+ y[i]*x[i]
                theta_0 = theta_0 + y[i]
            else:
                pass
    return (theta,theta_0)

#initialize parameters
x = np.array([[-1,-1],[1,0],[-1,1.5]])
y = np.array([1,-1,1])
T = 2

print(perceptron_origin(x,y,T))

