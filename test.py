# test file

# %%

import sympy


# %%
# Define the matrix
A = sympy.Matrix([
    [0, 1],
    [-1, 0]
])
theta = sympy.Symbol('theta')
# %%
B = sympy.exp(theta * A).simplify()
# %%
