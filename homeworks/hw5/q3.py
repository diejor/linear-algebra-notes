from numpy import *
from scipy.linalg import *

set_printoptions(precision=3)

A = array([
    [1, 0],
    [1, 2]
])

B = array([
    [3, 2],
    [0, 1]
])

A_T = transpose(A)
B_T = transpose(B)

print("A_T*B_T:")
print(A_T*B_T)
print()

print("B_T*A_T:")
print(B_T*A_T)
print()

print("transpose(A*B):")
print(transpose(A*B))
print()

A_inv = matrix(inv(A))
B_inv = matrix(inv(B))

print("A_inv:")
print(A_inv)

print("B_inv:")
print(B_inv)

print("B_inv*A_inv:")
print(B_inv*A_inv)
print()

print("B_inv:")
print(B_inv)
print("A_inv:")
print(A_inv)