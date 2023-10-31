from sympy import symbols, Matrix, Eq
import numpy as np
import matplotlib.pyplot as plt

# Define the symbols
a, b, c = symbols('a b c')

# Given data points
points = [(-2, 2), (0, 1), (1, 1), (2, 3)]

# Form the A matrix and B vector
A_list = [[1, point[0], point[0]**2] for point in points]
B_list = [[point[1]] for point in points]
A = Matrix(A_list)
B = Matrix(B_list)

# Print A and B
print("Matrix A:")
print(A)
print("\nVector B:")
print(B)

# Calculate using the normal equation
normal_eq_lhs = A.T * A
normal_eq_rhs = A.T * B

# Solve for the coefficients [a, b, c]
solution = normal_eq_lhs.LUsolve(normal_eq_rhs)

# Print the normal equation matrices and solution
print("\nNormal Equation LHS (A^T * A):")
print(normal_eq_lhs)
print("\nNormal Equation RHS (A^T * B):")
print(normal_eq_rhs)
print("\nSolution [a_hat, b_hat, c_hat]:")
print(solution)

# Extract a, b, and c values from the solution
a_hat, b_hat, c_hat = float(solution[0]), float(solution[1]), float(solution[2])

# Define the parabola function using the found coefficients
def parabola(x):
    return a_hat * x**2 + b_hat * x + c_hat

# Generate x values for the curve
x_values = np.linspace(-3, 3, 400)
y_values = [parabola(x) for x in x_values]

# Plotting the data points
x_data, y_data = zip(*points)
plt.scatter(x_data, y_data, color='red', label='Data Points')

# Plotting the best fit parabola
plt.plot(x_values, y_values, label='Best Fit Parabola', color='blue')

# Labelling the plot
plt.title('Best Fit Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
