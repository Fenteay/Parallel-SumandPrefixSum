import threading
import time
import numpy as np
import sys
sys.setrecursionlimit(10**6)

def mul(A, B):
    l = len(A)
    C = [[0 for row in range(l)] for col in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                C[i][j] += A[i][k] * B[k][j]
    return C

def calc(i, l, A, B, C):
    for j in range(l):    
        for k in range(l):
            C[i][j] += A[i][k] * B[k][j]

def parallelmul(A, B):
    l = len(A)
    # determine zero matrix
    C = [[0 for row in range(l)] for col in range(l)]
    for i in range(l):
        # parallel for i
        t =threading.Thread(target=calc,args=( i, l, A, B, C))
        t.start()
    t.join()
    return C

if __name__ == "__main__":
    n=10000
    M1 = np.random.randint(1,10,size=(n,n)).astype(np.int32)
    M2 = np.random.randint(1,10,size=(n,n)).astype(np.int32)
    print('Matrix 1:')
    print(M1)
    print('Matrix 2:')
    print(M2)
    t = time.time()
    result = np.array(mul((M1 , M2)))
    print("time seq:",time.time()-t)
    print(result)
    t1 = time.time()
    resultp = np.array(parallelmul(M1, M2))
    print('Result A * B:')
    print("time para:",time.time()-t1)
    print(resultp)
    if (np.array_equal(result,resultp)):
        print('Correct: True')
    else:
        print('Correct: False')