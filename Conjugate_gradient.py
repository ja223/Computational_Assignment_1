#Conjugate Gradient  Method 
import numpy as np 
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])#the given matrix
b=np.array([1,2,3,4,5])# the b vector of the given equation A*x=b
T=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])# Solution given in the question and it is the initial tolerance as the guessing initilal solution X=0
X=np.zeros(5)# guessing the intinal solution of X to be zero
V=b-np.matmul(A,X)#
W=V
count=0#iteration
for h in range(100):
    Q=np.matmul(np.transpose(V),V)/np.matmul(np.transpose(W),np.matmul(A,W))
    X=X+Q*W
    V_=V-Q*np.matmul(A,W)
    key=0
    for j in range(5):
        if (abs(X[j]-T[j])>=0.01):#According to the question the difference between T and and the approximate vector we get(X) after iteration is less than 0.01 
            key=1 #condition of the process to next iteration
    if(key==0):
        break
    
    P=np.matmul(np.transpose(V_),V_)/np.matmul(np.transpose(V),V)
    V=V_
    W=V+P*W
    count=count+1
if(key==1):
    print('The required accuracy is not reached after ',count,' iterations')
else:
    print(X,count+1)#count gives the number how many iterations required to achive this condition (difference  less than 0.01)


