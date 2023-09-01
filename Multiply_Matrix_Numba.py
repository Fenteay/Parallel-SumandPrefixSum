import time
from multiprocessing import Pool,cpu_count
import numpy as np
from numba import njit, prange
import sys
sys.setrecursionlimit(10**6)

@njit(parallel=True)
def mat_mult(A, B):
    assert A.shape[1] == B.shape[0]
    res = np.zeros((A.shape[0], B.shape[1]), )
    for i in prange(A.shape[0]):
        for k in range(A.shape[1]):
            for j in range(B.shape[1]):
                res[i,j] += A[i,k] * B[k,j]
    return res
if __name__=="__main__":
    n = 10000
    A = np.random.randint(1,10,size=(n,n)).astype(np.int32)
    B = np.random.randint(1,10,size=(n,n)).astype(np.int32)
    s = time.time()
    res = mat_mult(A, B)
    print("time parallel numba:",time.time()-s,"\n",res,"\n")
    s = time.time()
    r= A @ B
    print("time numpy:",time.time()-s,"\n",r,"\n")
    if (np.array_equal(res,r)):
        print('Correct: True')
    else:
        print('Correct: False')