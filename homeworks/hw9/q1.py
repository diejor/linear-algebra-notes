
from numpy import * 
# Given data
A = matrix([[1, 0], [1, 1], [1, 2], [1, 3]])
b = matrix([2, 1, -1, 2]).T

# Calculate x hat using the normal equation
AtA = A.T @ A
Atb = A.T @ b

print("A^TA:\n", AtA)
print("A^Tb:\n", Atb)

# Solve for x_hat
AtA_inv = linalg.inv(AtA)
print("A^TA inverse:\n", AtA_inv)

x_hat = AtA_inv @ Atb
print("x_hat:\n", x_hat)

# Extract C and D from x hat 
C, D = x_hat 

# Calculate predicted b values
b_hat = A @ x_hat
print("Value of C:", C)
print("Value of D:", D)
print("Predicted b values:\n", b_hat)
