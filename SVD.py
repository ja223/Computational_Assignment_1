#Singular value Decomposition Method 
#In this method  A real matrix of dimention(m,n) is decomposed through A=U*S*V^T , where the S is a real Diaginal matrix of dimention(m,n) and U, V are real othogonal matrics of dimention (m,m) and (n,n) respectivly
import numpy as np
import time
def invert(M):
	n=max(M.shape)
	N=np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			N[j][-i-1]=M[j][i]
	return(N)
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line row wise(separated by space): ")   
entries = list(map(int, input().split())) 
A = np.array(entries).reshape(R, C) 
print('The given matrix is:\n',A) 
start_time1=time.time() # start_time1 is the initial time for  SVD operation of the  matrix through numpy
U1,S1,V1=np.linalg.svd(A)# U1,V1,S1 are the decomposed  matrics through numpy.linalg.svd
print('Time required for result using numpy.linalg.svd = ',(time.time()-start_time1))
print('SVD form using np.linalg.svd: \n')
print('U1:\n',U1,'\n S1:\n',S1,'\n V1:\n',V1)
start_time2=time.time() # start_time2 is the initial time for  SVD operation of the  matrix through python3 code
eigen_value_1,eigen_vector_1=np.linalg.eigh(np.matmul(A,np.transpose(A)))# eigenvalues and eigen vectors of A*A^T
eigen_value_2,eigen_vector_2=np.linalg.eigh(np.matmul(np.transpose(A),A))#eigenvalues and eigen vectors of A^T*A
U=np.zeros(5)
V=np.zeros(3)
U2=np.zeros((5,5))
V2=np.zeros((3,3))
for i in range(5):
    U[i]=eigen_value_1[-i-1]
    for k in range(5):
        U2[k][-i-1]=eigen_vector_1[k][i]

for j in range(3):
    V[j]=eigen_value_2[-j-1]
    for l in range(3):
        V2[l][-j-1]=eigen_vector_2[l][j]
#eigen_1=eigen_value_1.argsort()[::-1]#sorting of eigen_value_1
#eigen_value_1=eigen_value_1[eigen_1]
#U2=eigen_vector_1[:,eigen_1] #sorting of eigen_vector_1 through eigen_value_1 ranks
#eigen_2=eigen_value_2.argsort()[::-1]#sorting of eigen_value_2
#eigen_value_2=eigen_value_2[eigen_2]
#V2=eigen_vector_2[:,eigen_2]#sorting of eigen_vector_1 through eigen_value_2 ranks
S2=np.matmul(np.matmul(np.transpose(U2),A),V2)
print('SVD form using python code: \n')
print('U2:\n',U2,'\n S2:\n',S2,'\n V2:\n',V2) # U2,V2,S2 are the decomposed  matrics through python3 code
print('Time required by SVD code= ',(time.time()-start_time2))
