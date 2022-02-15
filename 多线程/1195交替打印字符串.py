'''
Description: 
Author: Tjg
Date: 2022-02-15 19:29:18
LastEditTime: 2022-02-15 21:02:22
LastEditors: Please set LastEditors
'''
# 死循环
import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.m = 1
        self.lock = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while True:
            if self.m > self.n:
                break
            elif self.m % 3 == 0 and self.m % 5 != 0:
                with self.lock:
                    printFizz()
                    self.m += 1

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            if self.m > self.n:
                break
            elif self.m % 3 != 0 and self.m % 5 == 0:
                with self.lock:
                    printBuzz()
                    self.m += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
    	while True:
            if self.m > self.n:
                break
            elif self.m % 3 == 0 and self.m % 5 == 0:
                with self.lock:
                    printFizzBuzz()
                    self.m += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
    	while True:
            if self.m > self.n:
                break
            elif self.m % 3 != 0 and self.m % 5 != 0:
                with self.lock:
                    printNumber()
                    self.m += 1


# 四个信号量
# 每个线程都有各自的迭代量
# number线程分发信号量
import threading 
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n+1
        self.Fizz=threading.Semaphore(0)
        self.Fizzbuzz=threading.Semaphore(0)
        self.Buzz=threading.Semaphore(0)
        self.Num=threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 ==0 and i%5 !=0:
                self.Fizz.acquire()
                printFizz()
                self.Num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 !=0 and i%5==0:
                self.Buzz.acquire()
                printBuzz()
                self.Num.release()
    	  	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3==0 and i%5==0:
                self.Fizzbuzz.acquire()
                printFizzBuzz()
                self.Num.release()
    	
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            self.Num.acquire()
            if i%3==0 and i%5==0:
                self.Fizzbuzz.release()
            elif i%3==0:
                self.Fizz.release()
            elif i%5==0:
                self.Buzz.release()
            else:
                printNumber(i)
                self.Num.release()

