import numpy as np
from activation_functions.functions import identity_function, sigmoid


def init_network():
    network = {}
    network["W1"] = np.random.randn(2, 3)
    network["W2"] = np.random.randn(3, 2)
    network["W3"] = np.random.randn(2, 2)
    network["b1"] = np.random.randn(3)
    network["b2"] = np.random.randn(2)
    network["b3"] = np.random.randn(2)
    return network


def forward(network, activation_function, x):
    a1 = np.dot(x, network["W1"]) + network["b1"]
    a1 = activation_function(a1)
    a2 = np.dot(a1, network["W2"]) + network["b2"]
    a2 = activation_function(a2)
    a3 = np.dot(a2, network["W3"]) + network["b3"]
    y = identity_function(a3)
    return y


x = np.array([0, 0])
network = init_network()
y = forward(network, sigmoid, x)

print(y)