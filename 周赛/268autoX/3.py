'''
Description: 
Author: Tjg
Date: 2021-11-21 10:47:56
LastEditTime: 2021-11-21 11:19:24
LastEditors: Please set LastEditors
'''
# class RangeFreqQuery:

#     def __init__(self, arr: list[int]):
#         self.arr = arr

#     def query(self, left: int, right: int, value: int) -> int:
#         subArr = self.arr[left:right + 1]
#         return subArr.count(value)
from collections import defaultdict
class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.dictList = []
        freqDict = defaultdict(int)
        self.dictList.append(defaultdict(int))
        for i in arr:
            freqDict[i] += 1
            self.dictList.append(freqDict.copy())
            # print(self.dictList)
           
    def query(self, left: int, right: int, value: int) -> int:
            freq1 = self.dictList[left][value]
            freq2 = self.dictList[right + 1][value]
            freq = freq2 - freq1
            return freq


arr = [2,2,1,2,2]
r1 = RangeFreqQuery(arr)
'''
["RangeFreqQuery","query","query","query"]
[[[2,2,1,2,2]],[2,4,1],[1,3,1],[0,2,1]]
'''
print(r1.query(2,4,1))
print(r1.query(1,3,1))
print(r1.query(0,2,1))
