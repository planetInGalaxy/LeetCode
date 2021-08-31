'''
Description: 
Author: Tjg
Date: 2021-08-01 07:12:56
LastEditTime: 2021-08-01 07:55:00
LastEditors: Please set LastEditors
'''
# 数组 行列关系 哈希保存 特殊情况
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        l = 0
        ans = []
        ans_set = set()
        for i in mat:
            i.append(0)
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i] == 0 and j not in ans_set:
                    ans.append(j)
                    ans_set.add(j)
                    l += 1
                    if l == k:
                        return ans

# 二分 + 堆
import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r= 0, n - 1,
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 1:
                    l = mid + 1
                else:
                    r = mid - 1
            power.append((r, i))

        heapq.heapify(power)
        # print(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans

s1 = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 4
answer = s1.kWeakestRows(mat,k)
print(answer)
