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
    exp_x = np.exp(x - m)   # 위 식에 임의의 값을 빼거나 더해도 결과값은 같다를 이용해서 값을 줄임(e^100 -> e^2)
    return exp_x / np.sum(exp_x)    # 이렇게 하면 합이 1이 되어서 결과값이 확률이 된다


if __name__ == "__main__":      # 이 파일에서만 실행시켜야 작동하는 조건문
    a = softmax(np.array([-1, 2, 4]))
    print(sum(a))