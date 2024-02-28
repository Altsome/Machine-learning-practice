import numpy as np

a = np.array([[0, 1, 2],
              [2, 3, 4],
              [3, 4, 5]])
print(a.ndim)
print(a.shape)
print(a.size)

print("------")
b = np.array([0, 1, 2, 2, 3, 4, 3, 4, 5])
print(b.ndim)
print(b.shape)
print(b.size)
print(b)
print(b.reshape(1, b.size))
print(b.shape)