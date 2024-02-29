import numpy as np
from functions.loss_functions import cross_entropy_error
from functions.activation_functions import softmax
"""
이파일은 class만 담고 있는 파일이여서 독자적으로 실행히시킬 일이 X
-> 이 import path는 class를 부를 파일을 기준으로 설정해줘야함
"""


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):   # 배치를 위한 relu 순전파
        out = x.copy()
        self.mask = out <= 0
        out[self.mask] = 0
        return out

    def backward(self, d_out):  # relu 역전파
        d_out[self.mask] = 0    # x가 0보다 작으면 0, 0이상이면 1*d_out
        dx = d_out
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):   # sigmoid 순전파
        self.out = 1 / (1 + np.exp(-x))
        return self.out

    def backward(self, d_out):  # sigmoid 역전파
        return self.out * (1 - self.out) * d_out    # sigmoid 미분한 식은 (1 - a) * a, a는 sigmoid(x)값


class SoftmaxWithLoss:  # 항등함수는 오차제곱합을 손실함수로, softmax는 cross_entropy를 손실함수로 사용
    def __init__(self):
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        loss = cross_entropy_error(self.y, self.t)
        return loss

    def backward(self, d_out=1):    # softmax와 cross_entropy함수를 하나의 함수로 보고 미분하면 ((예측값 - 정답) / 정답 개수) 가 나옴
        batch_size = self.t.shape[0]
        return (d_out * (self.y - self.t)) / batch_size

