'''
Description: 
Author: Tjg
Date: 2021-07-25 07:49:07
LastEditTime: 2021-07-25 08:23:44
LastEditors: Please set LastEditors
'''
# 哈希
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        link = {}
        for i in adjacentPairs:
            link[i[0]] = link.get(i[0],[])
            link[i[0]].append(i[1])
            link[i[1]] = link.get(i[1],[])
            link[i[1]].append(i[0])
        print(link)
            
        nums = []
        for key,value in link.items():
            if len(value) == 1:
                nums.extend([key,value[0]])
                break
        print(nums)
        n = len(adjacentPairs)
        while len(nums) < n + 1:
            nearest_link = link[nums[-1]]
            print(nums[-1],nearest_link)
            if len(nearest_link) == 1:
                nums.append(nearest_link[0])
                break
            if nearest_link[0] == nums[-2]:
                nums.append(nearest_link[1])
            else:
                nums.append(nearest_link[0])
        return nums

s1 = Solution()
adjacentPairs = [[100000,-100000]]
answer = s1.restoreArray(adjacentPairs)
print(answer)