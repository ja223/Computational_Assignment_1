# QR decomposition method 

import numpy as np
import math
A=np.array([[5,-2],[-2,8]]) # the given matrix
C,D=np.linalg.eigh(A) # C= array of the eigenvalues and D=array of the eigenvectors
print(C)
print(D)
i=0        #i = iteration   
while  abs(A[0,1])>=10**-5 or abs(A[1,0])>=10**-5:# we need to iterate untill the off- diagonal terms becomes very small less than 10^(-5)
         Q,R=np.linalg.qr(A) # Decomposition of A into Q(orthogonal) and R(upper triangular)  (A(i+1)=Q(i)*R(i))
         A=np.matmul(R,Q)    #A(i)=R(i)*Q(i)
         i=i+1
print(i)                     # no of iteration required
QR_decomposition_eigenvale1=A[0,0]  # diagonals are the eigen values 
QR_decomposition_eigenvale2=A[1,1]
print(QR_decomposition_eigenvale1)
print(QR_decomposition_eigenvale2)

