from numpy import *
from scipy.linalg import *

set_printoptions(precision=3)

K_3 = array([
    [-2, 1, 0],
    [1, -2, 1],
    [0, 1, -2]
])

b = -(1./16)*array([[-1], 
           [1], 
           [-1]])

print("u vector solution:")
print(solve(K_3, b))