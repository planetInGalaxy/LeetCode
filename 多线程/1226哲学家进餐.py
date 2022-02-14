'''
Description: 
Author: Tjg
Date: 2022-02-14 21:24:27
LastEditTime: 2022-02-14 22:22:10
LastEditors: Please set LastEditors
'''
'''
哲学家进餐问题的关键在于解决进程死锁。
这些进程之间只存在互斥关系，但是与之前接触到的互斥关系不同的是，
每个进程都需要同时持有两个临界资源，因此就有“死锁”问题的隐患。
关键在于避免环路等待
'''

# 方法一
# 最多允许四个哲学家同时进餐。
# 这样可以保证至少有一个
# 哲学家是可以拿到左右两根筷子的
import threading
class DiningPhilosophers:
    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]
        self.quota = threading.Semaphore()
    
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        self.quota.acquire()
        with self.locks[philosopher]:
            with self.locks[(philosopher + 1) % 5]:
                pickLeftFork()
                pickRightFork()
                eat()
                putRightFork()
                putLeftFork()
        self.quota.release()


# 方法二
# 根据哲学家编号的奇偶性决定先拿左筷子还是右筷子
# 如果相邻的两个哲学家都想吃饭，那么只会有其
# 中一个可以拿起第一根筷子，另一个会直接阻塞。
# 哲学家在拿了第一根筷子后，如果拿另外一根被阻塞，
# 那另外一根筷子一定是其他哲学家拿的第二根筷子，
# 所以会很快解除阻塞。
import threading
class DiningPhilosophers:
    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]
        
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # 左右叉子的编号
        # right_fork = philosopher
        # left_fork = (philosopher + 1) % 5

        # # 偶数编号的先拿右边叉子
        # if philosopher % 2 == 0:
        #     self.locks[right_fork].acquire()
        #     self.locks[left_fork].acquire()
            
        # #奇数编号的先拿左边叉子
        # else:
        #     self.locks[left_fork].acquire()
        #     self.locks[right_fork].acquire()
        # pickLeftFork()
        # pickRightFork()
        # eat()
        # putLeftFork()
        # putRightFork()
        # self.locks[right_fork].release()
        # self.locks[left_fork].release()

        if philosopher % 2 == 0:
            with self.locks[philosopher]:
                with self.locks[(philosopher + 1) % 5]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putRightFork()
                    putLeftFork()
        else:
            with self.locks[(philosopher + 1) % 5]:
                with self.locks[philosopher]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putRightFork()
                    putLeftFork()

# 方法三
# 每次只允许一个哲学家拿筷子，直到他吃完
# 这样可以保证拿筷子的哲学家一定有两根筷子可用
import threading
class DiningPhilosophers:
    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]
        self.mutex = threading.Lock()
    
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        self.mutex.acquire()
        with self.locks[philosopher]:
            with self.locks[(philosopher + 1) % 5]:
                pickLeftFork()
                pickRightFork()
                eat()
                putRightFork()
                putLeftFork()
        self.mutex.release()

