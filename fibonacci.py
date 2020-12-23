fib=[x for x in range(20)]
for i in range(20):
    if i < 2:
        fib[i]=1
    else:
        fib[i]=fib[i-1]+fib[i-2]
    print (fib[i])

print("============{}===========".format("generator"))


def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a

for i in fib(20):
    print (i)


print("============{}===========".format("Iterator"))

class Fbb(object):
    """迭代器"""
    
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
   
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


print([j for j in Fbb(20)])


import time
import threading


#==========Fibonacci with multi-threading ===============

def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print ('COST: {:5f}'.format(end - start))
    return wrapper


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


@profile
def nothread():
    fib(35)
    fib(35)


@profile
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.currentThread()
    print(main_thread)
    for t in threading.enumerate():
        print (t)
        if t is main_thread:
            continue
        t.join()

nothread()
hasthread()

