'''
Description: 
Author: Tjg
Date: 2021-07-29 15:14:46
LastEditTime: 2021-11-24 09:38:01
LastEditors: Please set LastEditors
'''

# 先将二维数组排序 再转化为 300
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0],-x[1]))

        increase = []
        for size in envelopes:
            if not increase or size[1] > increase[-1][1]:
                increase.append(size)
            else:
                left,right = 0,len(increase)
                while left <= right:
                    mid = left + (right - left) // 2
                    if increase[mid][1] > size[1]:
                        right = mid - 1
                    elif increase[mid][1] < size[1]:
                        left = mid + 1
                    else:
                        break
                else:
                    increase[left] = size
        return len(increase)

s1 = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
answer = s1.maxEnvelopes(envelopes=envelopes)
print(answer)