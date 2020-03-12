#Power method 
#In power method we get the dominent eigenvalue and corresponding eigen vector of a matrix
import numpy as np 
import math
A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]]) #The given matrix
C,D=np.linalg.eigh(A) 
X0 = np.array([[1],[0],[0]]) # A general vector in real space
X1 =np.matmul(A,X0) 
error=0.01
norm1=np.matmul(np.transpose(X1),X1) # inner product of the vector A*X0
norm2=np.matmul(np.transpose(np.matmul(A,X1)),X1)# inner product of A*A*X0 and A*X0
eigenvalue0=norm2/norm1# this gives the initial  eigen value and the initial eigenvector is A*X0
i=0 # iteration
while abs((error)>= 0.01): #The answer should be acccurate upto one percent according to the Question 
        X1=np.matmul(A,X1)
        norm1=np.matmul(np.transpose(X1),X1)
        norm2=np.matmul(np.transpose(np.matmul(A,X1)),X1)
        eigenvalue1=norm2/norm1
        eigenvector=np.matmul(A,X1) #eigen vector after ith iteration
        norm=np.linalg.norm(eigenvector)# norm of the corresponding eigen vector 
        norm_eigenvector=eigenvector/norm # normalised eigenvector
        error=(eigenvalue1-eigenvalue0)/eigenvalue0  # the relative error =the differnce between two eigenvalues of two consecutive iteration devided by the eigen value after first iteration
        eigenvalue0=eigenvalue1  
        i=i+1
print(i)  # the max ietration upto which the above condition satisfied
print(eigenvalue1)
print(norm_eigenvector)
