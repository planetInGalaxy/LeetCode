'''
Description: 
给你一个会议时间安排的数组 intervals
每个会议时间都会包括开始和结束的时间
intervals[i] = [starti, endi]
返回所需会议室的最小数量。
Author: Tjg
Date: 2022-02-22 20:17:28
LastEditTime: 2022-02-22 20:36:16
LastEditors: Please set LastEditors
'''
# 优先队列（堆）
# 时间复杂度O(nlogn) 空间复杂度O(n)
# n = len(intervals)
import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if intervals is None or intervals == []:
            return None

        intervals.sort()
        rooms = []
        ans = 0
        heapq.heapify(rooms)
        for interval in intervals:
            while rooms and rooms[0] <= interval[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval[1])
            ans = max(ans, len(rooms))

        return ans