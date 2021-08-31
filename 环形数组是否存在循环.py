'''
Description: 
Author: Tjg
Date: 2021-08-07 21:07:35
LastEditTime: 2021-08-07 21:46:34
LastEditors: Please set LastEditors
'''
# 快慢指针
class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        # 保证返回值在 [0,n) 中
        def next(cur: int) -> int:
            return (cur + nums[cur]) % n  

        # 遍历每个节点
        for i, num in enumerate(nums):
            # 如果该节点，则说明无环，不用尝试了
            if num == 0:
                continue
            # 设置快慢指针
            slow, fast = i, next(i)
            # 判断非零且方向相同,fast跳两步，需要都检测
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                # 如果相遇则有环
                if slow == fast:
                    # 如果环的长度为1.则舍弃
                    if slow == next(slow):
                        break
                    # 环的长度大于1，符合题意
                    return True
                # 慢指针走一步，快指针走两步
                slow = next(slow)
                fast = next(next(fast))
            # 如果没环，重新遍历一遍，把走过的都置为0
            add = i
            while nums[add] * nums[next(add)] > 0:
                nums[add] = 0
                add = next(add)
        return False
