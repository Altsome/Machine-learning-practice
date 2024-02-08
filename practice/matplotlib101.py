from matplotlib import pyplot as plt
from network.activation_functions.functions import *

def draw_function(fn, x_range):
    y = fn(x_range)

    plt.plot(x_range, y)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

x_range = np.arange(-5, 5, 0.1)
draw_function(relu, x_range)