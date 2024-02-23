import numpy as np


def sum_squares_error(y, t):    # 오차제곱합
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    delta = 1e-7    # log0은 음의 무한대이므로 오류를 방지하기 위한 아주 작은 값

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y + delta)) / batch_size

# 정확도 대신 손실함수를 사용하는 이유 = 학습에서 미분을 해야하는데 정확도를 쓰면 대부분 미분값이 0이 나오기때문에 경사하강법이 적용이 안됨

