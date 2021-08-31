'''
Description: 
Author: Tjg
Date: 2021-08-06 22:13:48
LastEditTime: 2021-08-06 22:29:19
LastEditors: Please set LastEditors
'''
from collections import deque
# 状态压缩 + 广度优先搜索 疑问
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0
        
        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        
        return ans
