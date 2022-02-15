'''
Description: 
修改给出的类，以输出序列 "010203040506..." ，
其中序列的长度必须为 2n 。
Author: Tjg
Date: 2022-02-14 22:24:50
LastEditTime: 2022-02-15 18:01:43
LastEditors: Please set LastEditors
'''
def printNumber(n):
    print(n)

# 超时 
# 两把锁
# 先获取锁，再判断
import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.oddEnd = n if n % 2 == 1 else n - 1
        self.evenEnd = n if n % 2 == 0 else n - 1
        self.lock_zero = threading.Semaphore(1)
        self.lock_notzero = threading.Semaphore(0)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.m < self.n:
            self.lock_zero.acquire()
            printNumber(0)
            self.m += 1
            self.lock_notzero.release()
        # print("0 over")

                
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        # 这里不能用True, example：n = 1
        while self.m <= self.evenEnd > 0:
            self.lock_notzero.acquire()
            if self.m % 2 == 0:
                printNumber(self.m)
                self.lock_zero.release()
                if self.m == self.evenEnd:
                    break
            else:
                self.lock_notzero.release()
        # print("2 over")
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        # 这里不能用True, example：n = 1
        while self.m <= self.oddEnd:
            self.lock_notzero.acquire()
            if self.m % 2 == 1:
                printNumber(self.m)
                self.lock_zero.release()
                if self.m == self.oddEnd:
                    break
            else:
                self.lock_notzero.release()
        # print("1 over")
        

# 三把锁
# 设立oddFlag,决定释放哪把锁
import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.oddEnd = n if n % 2 == 1 else n - 1
        self.evenEnd = n if n % 2 == 0 else n - 1
        self.OddFlag = True
        self.lock_zero = threading.Semaphore(1)
        self.lock_odd = threading.Semaphore(0)
        self.lock_even = threading.Semaphore(0)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.m < self.n:
            self.lock_zero.acquire()
            printNumber(0)
            self.m += 1
            if self.OddFlag:
                self.lock_odd.release()
            else:
                self.lock_even.release()
            self.OddFlag = not self.OddFlag
        # print("0 over")

                
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        # 这里不能用True, example：n = 1
        while self.m <= self.evenEnd > 0:
            self.lock_even.acquire()
            printNumber(self.m)
            self.lock_zero.release()
            if self.m == self.evenEnd:
                break
        # print("even over")
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.m <= self.oddEnd:
            self.lock_odd.acquire()
            printNumber(self.m)
            self.lock_zero.release()
            if self.m == self.oddEnd:
                break
        # print("odd over")


s1 = ZeroEvenOdd(1)

threading.Thread(target=s1.even, args=(printNumber,)).start()

threading.Thread(target=s1.odd, args=(printNumber,)).start()

threading.Thread(target=s1.zero, args=(printNumber,)).start()
