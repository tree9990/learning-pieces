
print ("=====Following is multi-threading with semaphore======")
print ("\n"*2) 

import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)


def foo(tid):
    with sema:
        print ('{} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print ('{} release sema'.format(tid))


threads = []

for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n"*2)
print ("=====Following is multi-threading with lock======")
print ("\n" *2)


import time
from threading import Thread, Lock

value = 0
lock = Lock()


def getlock():
    global value
    with lock:
        new = value + 1
        time.sleep(0.001)
        value = new

threads = []

for i in range(100):
    t = Thread(target=getlock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print (value)


print("\n"*2)
print ("=====Following is multi-threading with Condition ======")
print("\n"*2)

import time
import threading

def consumer(cond):
    t = threading.currentThread()
    with cond:
        cond.wait()  # wait()方法创建了一个名为waiter的锁，并且设置锁的状态为locked。这个waiter锁用于线程间的通讯
        print ('{}: Resource is available to consumer'.format(t.name))


def producer(cond):
    t = threading.currentThread()
    with cond:
        print ('{}: Making resource available'.format(t.name))
        cond.notifyAll()  # 释放waiter锁，唤醒消费者


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()


print("\n"*2)
print ("=====Following is multi-threading with Event ======")
print("\n"*2)

import time
import threading
from random import randint


TIMEOUT = 2

def consumer(event, l):
    t = threading.currentThread()
    while 1:
        event_is_set = event.wait(TIMEOUT)
        if event_is_set:
            try:
                integer = l.pop()
                print ('{} popped from list by {}'.format(integer, t.name))
                event.clear()  # 重置事件状态
            except IndexError:  # 为了让刚启动时容错
                pass


def producer(event, l):
    t = threading.currentThread()
    while 1:
        integer = randint(10, 100)
        l.append(integer)
        print ('{} appended to list by {}'.format(integer, t.name))
        event.set()  # 设置事件
        time.sleep(1)


event = threading.Event()
l = []

threads = []

for name in ('consumer1', 'consumer2'):
    t = threading.Thread(name=name, target=consumer, args=(event, l))
    t.start()
    threads.append(t)

p = threading.Thread(name='producer1', target=producer, args=(event, l))
p.start()
threads.append(p)

for t in threads:
    t.join()


print("\n"*2)
print ("=====Following is multi-threading with Queue ======")
print("\n"*2)

import time
import threading
from random import random
from Queue import Queue

q = Queue()


def double(n):
    return n * 2


def producer():
    while 1:
        wt = random()
        time.sleep(wt)
        q.put((double, wt))


def consumer():
    while 1:
        task, arg = q.get()
        print (arg, task(arg))
        q.task_done()


for target in(producer, consumer):
    t = threading.Thread(target=target)
    t.start()


print("\n"*2)
print ("=====Following is multi-threading with Priority Queue ======")
print("\n"*2)

import time
import threading
from random import randint
from Queue import PriorityQueue


q = PriorityQueue()


def double(n):
    return n * 2


def producer():
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print ('put :{}'.format(pri))
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print ('[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg)))
        q.task_done()
        time.sleep(0.1)


t = threading.Thread(target=producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()

print("\n"*2)
print ("=====Following is multi-threading with thread pool ======")
print("\n"*2)

import time
import threading
from random import random
from Queue import Queue


def double(n):
    return n * 2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()
    def run(self):
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print ('USE: {}'.format(self.name))  # 线程名字
                print (f(*args, **kwargs))
            except Exception as e:
                print (e)
            self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=5):
        self._q = Queue(num_t)
        # Create Worker Thread
        for _ in range(num_t):
            Worker(self._q)
    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))
    def wait_complete(self):
        self._q.join()


pool = ThreadPool()
for _ in range(8):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)
pool.wait_complete()

