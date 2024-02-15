import numpy as np
from matplotlib import pyplot as plt
from network.functions.activation_functions import *


def draw_trigonometry():
    x = np.arange(-5, 5, 0.01)

    plt.plot(x, np.sin(x), linestyle="-", label="sin")
    plt.plot(x, np.cos(x), linestyle="--", label="cos")
    plt.axhline("y=0")
    plt.title("trigonometry")
    plt.legend()    # 데이터의 범례(라벨)을 표시
    plt.show()


def draw_function(fn, x):
    y = fn(x)

    plt.plot(x, y)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()


x_range = np.arange(-5, 5, 0.1)
# draw_function(relu, x_range)

draw_trigonometry()