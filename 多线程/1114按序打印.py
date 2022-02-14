'''
Description: 
请设计修改程序，
以确保second()方法在first()方法之后被执行，
third()方法在second()方法之后被执行。
Author: Tjg
Date: 2022-02-14 21:16:00
LastEditTime: 2022-02-14 21:22:43
LastEditors: Please set LastEditors
'''
# 信号量
import threading
class Foo:
    def __init__(self):
        self.sec_lock = threading.Semaphore(0)
        self.thr_lock = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sec_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.sec_lock.acquire()
        printSecond()
        self.thr_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.thr_lock.acquire()
        printThird()

# 官方
# Lock 锁
from threading import Lock
class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()
