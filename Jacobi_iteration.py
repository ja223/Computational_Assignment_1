#Jacobi Method 
# In this method the given matrix can be written A=D(diagonal)-L(strictly lower traingular)-U(strictly upper triangular) and the soulution of the equation A*x=b is  X(k+1)=D^(-1)*(L+U)*X(k)+D^(-1)*b   where k is the iteration 
import numpy as np
from numpy.linalg import inv
A=np.array([[0.2,0.1,1.0,1.0,0.0],[0.1,4.0,-1.0,1.0,-1.0],[1.0,-1.0,60.0,0.0,-2.0],[1.0,1.0,0.0,8.0,4.0],[0.0,-1.0,-2.0,4.0,700.0]])# The given matrix
b=np.array([1.0,2.0,3.0,4.0,5.0]) # the b vector of the given equation A*x=b
T=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])# Solution given in the question and it is the initial tolerance as the guessing initilal solution X=0
X=np.array([0,0,0,0,0])# guessing the intinal solution of X to be zero
D=np.diag([0.2,4.0,60.0,8.0,700.0])# diagonal matrix 
U=np.triu(-A,1)# Strictly upper triangular 
L=np.tril(-A,-1)# Strictly lower triangular 
D_=np.linalg.inv(D) #D_ is the inverse of D via numpy.linalg.inv
count=0 #iteration
key=0
for h in range(100):
    if(key==1):  #condition of the process to next iteration  
        X=np.matmul(D_,np.matmul((L+U),X))+np.matmul(D_,b) #solution after next iteration 
        count=count+1
    key=0
    for k in range(5):            
        if(abs(X[k]-T[k])>=0.01):#According to the question the difference between T and and the approximate vector we get(X) after iteration is less than 0.01 
            key=1
            
if(key==1):
    print('The required accuracy is not reached after ',count,' iterations')
else:
    print(X,count) #count gives the number how many iterations required to achive this condition (difference  less than 0.01)

