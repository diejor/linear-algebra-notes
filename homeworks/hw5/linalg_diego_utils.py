from numpy import *
from scipy.linalg import *

def elimination_matrix(pivot, row, A):
    E = identity(A.shape[0])
    has_pivot = True
    if (A[pivot,pivot] == 0):
        print("Error: pivot is zero")
        return None;
    E[row, pivot] = -A[row,pivot]/A[pivot,pivot]
    return E

def elimination_matrices_from(A):
    A = matrix(A)
    n = A.shape[0]
    m = A.shape[1]
    if (n != m):
        print("Error: matrix is not square")
        return None;
    Es = []

    for pivot in range(n):
        for row in range(pivot+1, n):
            E = [elimination_matrix(pivot, row, A)]
            A = E*A
            Es += E
    return Es

def upper_trigangular_from(A):
    Es = elimination_matrices_from(A)
    U = A.copy()
    for E in Es:
        U = E*U
    return U


def lower_triangular_from(A):
    Es = elimination_matrices_from(A)
    L = eye(A.shape[0])
    for E in reversed(Es):
        E_inv = matrix(inv(E))
        L = E_inv*L
    return L

def elim_matrix_from_lower(L):
    n = L.shape[0]
    Es = []

    for pivot in range(n):
        for row in range(pivot+1, n):
            E = identity(n)
            E[row, pivot] = -L[row,pivot]
            Es += [E]
    return Es
    
