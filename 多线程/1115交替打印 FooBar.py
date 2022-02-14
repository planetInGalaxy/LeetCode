'''
Description: 
两个不同的线程将会共用一个 FooBar 实例：
线程 A 将会调用 foo() 方法，
而线程 B 将会调用 bar() 方法，
请设计修改程序，以确保 "foobar" 被输出 n 次。
Author: Tjg
Date: 2022-02-14 20:53:37
LastEditTime: 2022-02-14 20:54:48
LastEditors: Please set LastEditors
'''
# 锁
import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Semaphore(1)
        self.bar_lock = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()


# 信号量
import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Semaphore(1)
        self.bar_lock = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()