import numpy as np
import sys, os
sys.path.append(os.pardir)
from functions.activation_functions import sigmoid
from functions.activation_functions import softmax
from functions.loss_functions import cross_entropy_error
from functions.gradient import numerical_gradient


class Net:
    def __init__(self, input_size, hidden_size, output_size):
        self.parameter = {}
        self.parameter["W1"] = 0.01 * np.random.randn(input_size, hidden_size)
        self.parameter["b1"] = np.zeros(hidden_size)
        self.parameter["W2"] = 0.01 * np.random.randn(hidden_size, output_size)
        self.parameter["b2"] = np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.parameter["W1"], self.parameter["W2"]
        b1, b2 = self.parameter["b1"], self.parameter["b2"]
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss




    # def accuracy(self, x, t):



if __name__ == "__main__":
    net = Net(2, 20, 30)
    x = np.array([0.6, 0.9])
    y = net.predict(x)
    print(y)
    print(net.loss(x, np.array([1, 0, 0])))
