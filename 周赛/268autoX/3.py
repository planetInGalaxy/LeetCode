'''
Description: 
Author: Tjg
Date: 2021-11-21 10:47:56
LastEditTime: 2021-11-22 07:32:17
LastEditors: Please set LastEditors
'''
# class RangeFreqQuery:

#     def __init__(self, arr: list[int]):
#         self.arr = arr

#     def query(self, left: int, right: int, value: int) -> int:
#         subArr = self.arr[left:right + 1]
#         return subArr.count(value)

# from collections import defaultdict
# class RangeFreqQuery:

#     def __init__(self, arr: list[int]):
#         self.dictList = []
#         freqDict = defaultdict(int)
#         self.dictList.append(defaultdict(int))
#         for i in arr:
#             freqDict[i] += 1
#             self.dictList.append(freqDict.copy())
#             # print(self.dictList)
           
#     def query(self, left: int, right: int, value: int) -> int:
#             freq1 = self.dictList[left][value]
#             freq2 = self.dictList[right + 1][value]
#             freq = freq2 - freq1
#             return freq

import bisect
class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.pos = [[] for i in range(100001)]
        for i in range(len(arr)):
            self.pos[arr[i]].append(i)
           
    def query(self, left: int, right: int, value: int) -> int:
        print(self.pos[value])
        # python二分查找模块
        # https://docs.python.org/zh-cn/3.6/library/bisect.html
        # 在[0,1,2,3,3,3,4]中查询3，分别返回3,6
        # 左闭右开
        # bisect_left是使>=i的所有值都>=value的最小i
        freq1 = bisect.bisect_left(self.pos[value], left)
        # bisect_right是使>=i的所有值都>value的最小i
        freq2 = bisect.bisect_right(self.pos[value], right)
        print(freq1, freq2)
        freq = freq2 - freq1
        return freq


arr = [0,1,2,3,4,0,1,2,3,4]
r1 = RangeFreqQuery(arr)
'''
["RangeFreqQuery","query","query","query"]
[[[0,1,2,3,4,0,1,2,3,4]],[2,6,1],[1,3,1],[0,8,2]]
'''
print(r1.query(2,6,1))
print(r1.query(1,3,1))
print(r1.query(0,8,2))
