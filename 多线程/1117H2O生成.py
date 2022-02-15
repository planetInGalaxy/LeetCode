'''
Description: 
这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
你必须保证产生一个水分子所需线程的结合必须发生在
下一个水分子产生之前。
Author: Tjg
Date: 2022-02-15 20:40:54
LastEditTime: 2022-02-15 21:48:03
LastEditors: Please set LastEditors
'''
# 信号量
# 根据不同条件释放不同数量信号量
import threading
class H2O:
    def __init__(self):
        self.hydrogen_mutex = threading.Semaphore(2)
        self.oxygen_mutex = threading.Semaphore(1)
        self.count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_mutex.acquire()
        releaseHydrogen()
        self.count += 1
        if self.count == 2:
            self.oxygen_mutex.release()
            self.count = 0


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_mutex.acquire()
        releaseOxygen()
        self.hydrogen_mutex.release(2)

        
