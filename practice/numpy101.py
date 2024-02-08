from network.activation_functions.functions import *

a = np.array([5, 4, 3, 2, 1])
print(a[a % 2 == 0]) #boolean indexing

print(step_funcion(np.array([1, 2, 3, -1])))
