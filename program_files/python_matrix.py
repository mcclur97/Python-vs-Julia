#import matplotlib.pyplot as plt
import random
import pandas as pd
#import numpy as np
import time

def matrix_create(n,m):
    '''This function takes in the desired dimensions for the matrices and creates
    two random matrices full of integers from 0 to 10, and one result matrix full of zeroes. 
    The matrices created are always able to be multiplied together.
    n = size of first dimension
    m = size of second dimension
    returns: two random matrices and result matrix'''
    

    a = [[random.randint(0, 10) for i in range(n)] for j in range(m)]
    b = [[random.randint(0, 10) for i in range(m)] for j in range(n)]
    answer = [[random.randint(0, 0) for i in range(m)] for j in range(n)]
    
    #List comprehension sourced from: https://www.dreamincode.net/forums/topic/413327-creating-nxm-matrix-without-numpy/
    return a, b, answer


#Create a time array for storing the different times of calculation
times = []

#Loop through matrices of size 100x100 to 3000x3000 by increments of 100 and record calculation time 
for n in range(100,300,100):
    #Unpack the randomly created ixi matrices 
    a, b, answer = matrix_create(n,n)
    
    #Time the calculation by taking an inital and final time
    t0 = time.time()
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                answer[i][j] += a[i][k] * b[k][j]
    t1 = time.time()

    #Add calculated time to time list
    times.append(t1-t0)
    
    #print the results of the calculation
    print('Time for calculation of',n,'x',n,'matrix:',t1-t0,'seconds')
    
julia_times = pd.read_csv("JuliaTimes.csv", header = None)

matrices2 = np.arange(100, 300, 100)

fig = plt.figure(figsize=(15,8))
plt.plot(matrices2, times[0:2], label = 'Python')
plt.plot(matrices2,julia_times[0:2], label ='Julia')
plt.legend()
plt.grid()
plt.title('Matrix Computation (Python vs Julia)', size = 20)
plt.ylabel('Time (s)')
plt.xlabel('Matrix size (NxN)')
fig.savefig('Speed_comparison.png')