'''
Description: 
数组 people 表示队列中一些人的属性，不一定按顺序。
每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，
前面正好有 ki 个身高大于或等于 hi 的人。
Author: Tjg
Date: 2022-02-19 17:26:22
LastEditTime: 2022-02-19 17:55:48
LastEditors: Please set LastEditors
'''
# 贪心 排序
# 时间复杂度O(n2) 空间复杂度O(logn)
# （若不包含输入输出，则只有排序的调用栈占了较大空间）
# 先考虑身高都不同的情况
# poeple根据身高升序排列
# 开一个len(people)大小的数组为ans
# 遍历people，把当前元素放到ans中第x+1个空位处
# x即为当前元素前面比他高的的人数
# 由于低的对后面没有影响，所以只计算空位处即可
# 如果有身高相同的，在占了空位之后
# 会影响到身高相同的且排在他后面的
# 所以再在之前排序基础上根据前面人数降序排列
# 这样就会先处理身高相同中的靠后位置，不会对前面有影响
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if people is None or people == [] or people == [[]]:
            return None

        people.sort(key=lambda x:(x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]

        for p in people:
            spaces = p[1]
            for i in range(n):
                if not ans[i]:
                    if spaces == 0:
                        ans[i] = p
                        break
                    spaces -= 1
        
        return ans