'''
Description: 
Author: Tjg
Date: 2021-07-16 14:21:29
LastEditTime: 2021-07-16 14:51:52
LastEditors: Please set LastEditors
'''
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        f = lambda x:x[0]
        intervals.sort(key=f)
        print(intervals)
        answer_list=[]
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] <= right:
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                answer_list.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]
            if i == len(intervals) - 1:
                answer_list.append([left,right])
            print(i,answer_list)

        return answer_list

# 思路更清晰
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


s1 = Solution()
intervals = [[1,2]]
answer = s1.merge(intervals)
print(answer)