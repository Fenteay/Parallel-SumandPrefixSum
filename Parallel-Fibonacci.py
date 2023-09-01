from multiprocessing import Pool
import time
import sys
sys.setrecursionlimit(10**6)
arrfi = []
def Fibonacci(n):
    for i in range(0,n+1):
        if i==0 or i==1:
            arrfi.append(i)
        else:
            arrfi.append(arrfi[i-1] + arrfi[i-2])
    return arrfi[n]
def ParallelFibonacci(n):
    listF=[n-1,n-2]
    pool=Pool(2)
    result=pool.map(Fibonacci,listF)
    return sum(result)
if __name__ == "__main__":
    n=1000
    start = time.time()
    print("Fibonacci 1000th with non-parallel:",Fibonacci(n))
    print("Finish in",(time.time()-start),"s")

    start2 = time.time()
    result = ParallelFibonacci(n)
    print("Fibonacci 1000th with non-parallel:",result)
    print("Finish in",(time.time()-start2),"s")
