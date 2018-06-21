import time
import itertools
import numpy as np
import matplotlib.pyplot as plt

#function to replace all elements of SAT with boleaan operators -----------
def replace_SAT_elements(M,x_array):
    n = M.shape[0]
    m = M.shape[1]
    N = np.zeros((n,m))
    for i in range(0,n):
        for j in range(0,m):
            if M[i,j] == 1:
                N[i,j]=x_array[j]

            elif M[i,j] == -1:
                N[i,j]= int(not x_array[j])

            else:
                N[i,j]=-1
    return N

#function to get the value of classifiers ---------------------------------
def getClassifiers(Y):
        C = np.zeros(Y.shape[0])
        for i in range(0,Y.shape[0]):
            #extracting the first row
            y = Y[i]
            #applying the boolean operation
            if any(t==1 for t in y):
                C[i] = 1
            elif all(t==-1 for t in y):
                C[i] = -1
            else:
                C[i] = 0
        return(C)


#function to get result by applying AND on classifiers----------------------  
def getResults(C):
    if any(q==0 for q in C):
        R = 0
    elif all(q==-1 for q in C):
        R = -1
    else:
        R = 1
    return(R)

  
#M is the input numpy matrix-------------------------------------------------
def SAT(M):
    c = 0
    count = 0
    #X contains the list of all the possible combinations of x1,x2,....xm
    X = [list(i) for i in itertools.product([0, 1], repeat = M.shape[1])]
    X = np.asarray(X)
    for i in range(0,X.shape[0]):
        #extracting the row of the matrix (x1,x2,x3...xm ---> one of the 2^m boolean combinations)
        x = X[i]

        #replace M matrix with Y on which we will perform boolean operations to check 
        Y = replace_SAT_elements(M,x)
        
        #now check elements to get value of classifiers
        C = getClassifiers(Y)
        
        #now check all classifiers to see if the value of x is true
        R = getResults(C)

        if R == 1:
            print("solution exists")
            print("here it is:")
            print(x)
            print(" ")
            c= 1
            count = count + 1
    if(c==0):
        print("no solution exists for this matrix M")

    print("The no. of solutions are")
    print(count)
                 

M = np.array([[1,1,0],[-1,1,0],[0,0,1]])  
SAT(M)

#MAKING THE GRAPH----------------------------------------------------------------------------------------
#fixing n=12 and looping from m=10 to m=25---------------------------------------------------------------
##n = 12
##time_array = np.zeros(11)
##for m in range(10,21):
##    M = np.random.randint(2, size=(n , m))
##    t0 = time.time()
##    SAT(M)
##    t1 = time.time()
##    time_array[m-10] = t1-t0
##
##plt.plot(time_array)
##plt.ylabel('time taken to run code')
##plt.xlabel('no. of columns in matrix M (m)')
##plt.show()
#-------------------------------------------------------------------------------------------------------          
            
    


        
    
