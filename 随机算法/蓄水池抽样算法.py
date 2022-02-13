'''
Description: 
随机算法面试题：https://juejin.cn/post/6844903686238371847
给定一个数据流，数据流长度N很大，
且N直到处理完所有数据之前都不可知，
请问如何在只遍历一遍数据, 即O(N)的情况下，
能够随机选取出m个不重复的数据。
Author: Tjg
Date: 2022-02-13 19:24:25
LastEditTime: 2022-02-13 22:26:04
LastEditors: Please set LastEditors
'''
import random
def reservoirSampling(nums, m):
    if nums is None:
        return None
    
    if len(nums) <= m:
        return nums

    ans = []
    for i in range(len(nums)):
        if i < m:
            ans.append(nums[i])
        else:
            randIdx = random.randint(0, i)
            if randIdx < m:
                ans[randIdx] = nums[i]

    return ans


nums = [random.randint(1, 100) for _ in range(10)]
m = 5
print(nums)

ans = reservoirSampling(nums, m)
print(ans)


    


    