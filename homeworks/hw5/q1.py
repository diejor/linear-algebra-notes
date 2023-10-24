from numpy import *
from scipy.linalg import *
from linalg_diego_utils import *

set_printoptions(precision=3)

A = matrix([
    [1,3,2],
    [3,7,5],
    [2,5,8]
])

P, L, U = lu(A)

Es = elim_matrix_from_lower(L)

for E in Es:
    print(E)
    print()