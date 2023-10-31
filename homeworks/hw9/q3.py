from sympy import Matrix, sqrt

# Given vectors
a = Matrix([3, 2, 5, 1])
b = Matrix([4, 3, 8, 3])

# Gram-Schmidt process
u1 = a
c = (b.dot(u1) / u1.dot(u1))
print("c:", c)
u2 = b - (b.dot(u1) / u1.dot(u1)) * u1
print("u1:\n", u1)
print("u2:\n", u2)

# Orthonormalize
q1 = u1 / u1.norm()
q2 = u2 / u2.norm()

print("Orthonormal q1:\n", q1)
print("Orthonormal q2:\n", q2)

# Vector to be projected
v = Matrix([0, 1, 2, 1])

# Projection onto the plane spanned by q1 and q2
av_proj = v.dot(q1) 
bv_proj = v.dot(q2)

print("Projection of v onto a:", av_proj, " or ", av_proj.evalf())
print("Projection of v onto b:", bv_proj, " or ", bv_proj.evalf())

