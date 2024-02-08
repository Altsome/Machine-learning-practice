import numpy as np


def step_function(x):
    y = x > 0
    return y.astype(np.int32)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    # 브로드캐스팅 가능


def relu(x):
    return np.maximum(x, 0)


def identity_function(x):
    return x


def softmax(x):
    m = np.max(x)
    exp_x = np.exp(x - m)
    return exp_x / np.sum(exp_x)


if __name__ == "__main__":      # 이 파일에서만 실행시켜야 작동하는 조건문
    a = softmax(np.array([-1, 2, 4]))
    print(sum(a))