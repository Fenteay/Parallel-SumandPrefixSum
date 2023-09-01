from multiprocessing import Process, cpu_count, Pool, Array
import timeit
from ctypes import c_int64

def Sum(l):
    sum = 0
    for i in range(1, l + 1):
        sum += i
    return sum

def ParallelSum(l):
    np = cpu_count()
    p = Pool(np) 
    sum = p.map(Sum, range(1, int(l) + 1))
    r = sum[10000-1:]
    p.close
    p.join
    print("\nParallel of Sum :", r)

def Prefixsum(array, l):
    for i in range(1, l):
        array[i] += array[i-1]
    return array

def Offset(array, s, t, offset):
    for i in range(s, t):
        array[i] += offset

def SubArrPrefixsum(array, start, end):
    for i in range(start+1, end):
        array[i] += array[i-1]

def ParallelPrefixsum(array, l):
    if l < 2:
        return Prefixsum(array, l)
    
    np = cpu_count()
    step = int(l/np)
    arr_p = []
    offset = 0
    
    if l % np:
        step += 1
    
    array = Array(c_int64, array, lock=False)
    
    for p in range(np):
        start = p*step
        stop = start+step
        if stop > l:
            stop = l   
        arr_p.append(Process(target=SubArrPrefixsum, args=(array, start, stop)))
    
    for p in range(np):    arr_p[p].start()
    for p in range(np):    arr_p[p].join()

    arr_p.clear()
    for sub_array in range(1, np):
        offset += array[sub_array*step-1]
        s_sub_array = sub_array*step
        e_sub_array = s_sub_array+step
        arr_p.append(Process(target=Offset,args=(array, s_sub_array, e_sub_array, offset)))
    
    for p in range(0, np-1):    arr_p[p].start()
    for p in range(0, np-1):    arr_p[p].join()
    return array[:]

if __name__ == "__main__":
    
    arr=[i for i in range(1, 10001)]
    l=10000
    print("Sum and Prefixsum 10000 of element from 1 to 10000:")
    start_processing = timeit.default_timer()
    print("\nNon-parallel Sum result:",Sum(l))
    print("Sum done in",(timeit.default_timer()-start_processing), "second")

    start_processing = timeit.default_timer()
    ParallelSum(l)
    print("ParallelSum done in",(timeit.default_timer()-start_processing), "second")

    start_processing = timeit.default_timer()
    prefixsum_nonparallel_array = Prefixsum(arr, l)
    print("\nNon-parallel Prefixsum result:", prefixsum_nonparallel_array[:])
    print("Prefixsum done in", timeit.default_timer()-start_processing, "second")
    
    start_processing = timeit.default_timer()
    prefixsum_parallel_array = ParallelPrefixsum(array=[i for i in range(1, 10001)], l=10000)
    print("\nMultiprocessing parallel Prefixsum result:", prefixsum_parallel_array[:])
    print("Parallel of Prefixsum with multiprocessing done in", timeit.default_timer()-start_processing, "second\n")
    



