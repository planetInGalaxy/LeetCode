'''
Description: 
15
38
Author: Tjg
Date: 2021-07-23 15:24:22
LastEditTime: 2021-07-23 15:56:37
LastEditors: Please set LastEditors
'''
# 坑点：需要先排序
# 迭代法 先找到包含左值的区间，再不断更新max_right的值
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda i:i[0])
        i = 0
        while i < len(ranges):
            if ranges[i][0] <= left and right <= ranges[i][1]:
                return True
            if ranges[i][0] <= left and ranges[i][1] >= left:
                max_right = ranges[i][1]
                i += 1
                break
            i += 1
        else:
            return False
        
        while i < len(ranges):
            if ranges[i][1] > max_right and ranges[i][0] <= max_right + 1:
                max_right = ranges[i][1]
            i += 1
        if max_right >= right:
            return True
        else:
            return False
s1 = Solution()
ls1 = [[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]
left = 15
right = 38
answer = s1.isCovered([[1,2]],left,right)
print(answer)