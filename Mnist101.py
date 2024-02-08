from matplotlib import pyplot as plt
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# print(x_train[0].shape)
# plt.imshow(x_train[0][0])
# plt.show()
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)

