import numpy as np
from matplotlib import pyplot as plt


def numerical_diff(f, x):   # 수치미분(근사치를 구함)
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)


# 기울기 구함
def numerical_gradient(f, x):   # 편미분
    h = 1e-4
    flattened = x.reshape(-1)
    grad = np.zeros_like(flattened)     # X와 같은 형상의 배열을 생성
    for idx in range(flattened.size):
        init_x = flattened[idx]
        flattened[idx] = init_x + h
        fxh1 = f(x)
        flattened[idx] = init_x - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        flattened[idx] = init_x

    grad = grad.reshape(x.shape)
    return grad


# 학습
def gradient_descent(f, init_x, lr=0.1, step_num=100):     # lr = 학습률
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
        plt.scatter(x[0], x[1])
    return x


if __name__ == "__main__":
    def function_2(x):
        return x[0]**2 + x[1]**2
    print(gradient_descent(function_2, np.array([3.0, 4.0])))
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.show()
