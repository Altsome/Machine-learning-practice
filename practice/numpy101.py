from network.functions.activation_functions import *

a = np.array([5, 4, 3, 2, 1])
print(a[a % 2 == 0])    # boolean indexing

print(step_function(np.array([1, 2, 3, -1])))
