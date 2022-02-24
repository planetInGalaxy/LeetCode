'''
Description: 
给你一个变量对数组 equations 
和一个实数值数组 values 作为已知条件，
其中 equations[i] = [Ai, Bi] 和 values[i] 
共同表示等式 Ai / Bi = values[i] 。
每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，
其中 queries[j] = [Cj, Dj] 表示第 j 个问题，
请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回所有问题的答案。如果存在某个无法确定的答案，
则用 -1.0 替代这个答案。
如果问题中出现了给定的已知条件中没有出现的字符串，
也需要用 -1.0 替代这个答案。
Author: Tjg
Date: 2022-02-24 20:49:02
LastEditTime: 2022-02-24 21:58:35
LastEditors: Please set LastEditors
'''
# dfs + 二值标记 + 哈希
# 时间复杂度 O(ml + q(m+l))
# 构建图时，需要处理 m 条边，
# 每条边都涉及到长为 l 的字符串比较
# 处理查询时，每次查询首先要进行一次 l 的比较，
# 然后至多遍历 m 条边。
# 空间复杂度O(nl + ml)
# 为了保存所有字符串节点，需要开辟空间为 nl 的哈希表（集合）
# 为了保存所有边和权重，需要开辟空间为 ml 的哈希表（字典）
# 处理查询时，还需要 n 的空间维护访问队列。
# n 节点（字符串）的数量 m 边的数量 
# q 查询次数 l字符串的平均长度
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node, value):
            if node == end:
                return value
            # print(node, visit[node], visit)
            if visit[node] != 0:
                return -1
            
            for edge in graph[node]:
                visit[node] = 1
                ans = dfs(edge[0], value * edge[1])
                visit[node] = 0
                if ans != -1:
                    return ans
            return -1
                
        graph = defaultdict(list)
        nodes = set()
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
            nodes.add(equations[i][0])
            nodes.add(equations[i][1])
        # print(nodes, graph)

        res = []
        for q in queries:
            if q[0] not in nodes or q[1] not in nodes:
                ans = -1
            else:
                start = q[0]
                end = q[1]
                visit = defaultdict(int)
                ans = dfs(start, 1)
            res.append(ans)
        
        return res





equations = [["a","e"],["b","e"]]
values = [4.0,3.0]
queries = [["a","b"],["e","e"],["x","x"]]
s1 = Solution()
ans = s1.calcEquation(equations, values, queries)
print(ans)