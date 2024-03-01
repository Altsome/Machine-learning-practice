import numpy as np


class Affine:    # 일반적인 y = xw + b 네트워크
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.dW = None
        self.db = None
        self.x = None

    def forward(self, x):   # 계산한 결과를 return(순전파)
        self.x = x
        y = np.dot(x, self.W) + self.b
        return y

    def backward(self, d_out):  # 위 층으로부터 온 기울기를 받아서 다시 x에 대한 기울기를 return
        self.dW = np.dot(self.x.T, d_out)   # Affine layer의 가중치 기울기
        self.db = np.sum(d_out, axis=0)     # Affine layer의 편향 기울기
        dx = np.dot(d_out, self.W.T)
        return dx

