import threading
import numpy as np
from multiprocessing import Pool

def shuffle(a,b):
    c = b.pop(0)
    a[c[0]], a[c[1]] = a[c[1]],a[c[0]]
    return a

def filter(b):
    i = 1    
    init = 0
    check = True
    while check :
        for x in b:
            if (x[0] == x[1]):
                b.pop(init)
                break
            for y in b[i:]:
                if (x[0] == y[1] or x[1] == y[0] or x[0] == y[0] or x[1] == y[1]):
                    b.pop(i)
                else:
                    i += 1
            init += 1
            i = init + 1
            if (init == len(b)):
                check = False

if __name__ == "__main__":
    b = list(np.random.randint(1000,size=(1000,2)))
    filter(b)
    a = np.array(range(1,1001))
    print("Array default:\n",a)
    
    threads = list()
    for i in range(len(b)):
        t = threading.Thread(target = shuffle, args=(a, b))
        threads.append(t)
        t.start()
    for index, thread in enumerate(threads):
        thread.join()
    
    print("\nArray after shuffle:\n",a)
