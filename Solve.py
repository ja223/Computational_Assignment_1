import numpy as np
A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]]) # A=the matrix
b=np.array([2,2,2])# the vector(b) of the matrix equation Ax=b
B=np.linalg.solve(A,b)# the solution
print(B)

