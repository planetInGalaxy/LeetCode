'''
Description: 
Author: Tjg
Date: 2021-08-02 16:19:48
LastEditTime: 2021-08-11 12:17:26
LastEditors: Please set LastEditors
'''
# dijkstra(贪心) 枚举
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 转化为邻接矩阵 空间复杂度O（n2）
        edges = [[float('inf')] * n for _ in range(n)]
        for start,end,dist in times:
            edges[start - 1][end - 1] = dist
        # 初始化最短距离表，因为是从k节点开始的，k->k的距离为0，
        # 因为start的选择取决于距离，故k即为初始节点
        shortest_dists = [float('inf')] * n
        shortest_dists[k - 1] = 0
        # 初始化访问表，已经访问的不再访问
        used = [False] * n
        # 一轮访问一个节点，一共访问n个节点，故循环n轮
        for _ in range(n):
            # 初始化为-1
            start = -1
            # 遍历访问表，如果没被访问过，并且该节点当初始节点的距离是当前最短的，则访问该节点
            for end,is_used in enumerate(used):
                if not is_used and (start == -1 or shortest_dists[end] < shortest_dists[start]):
                    start = end
            # 访问该节点，并且更新与其相邻的节点到初始节点的最短距离
            for end,dist in enumerate(edges[start]):
                shortest_dists[end] = min(shortest_dists[end], shortest_dists[start] + dist)
            # 标记为已访问
            used[start] = True
        # 最远的即为答案
        ans = max(shortest_dists)
        # 无解则返回 -1
        return ans if ans != float('inf') else -1

# dijkstra 最小堆
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 邻接表 空间复杂度O（m + n）
        g = [[] for _ in range(n)]
        for x, y, time in times:
            g[x - 1].append((y - 1, time))
        # 初始化最短距离表，因为是从k节点开始的，k->k的距离为0，
        # k即为初始节点
        print(g)
        dist = [float('inf')] * n
        dist[k - 1] = 0
        # 初始化最小堆，先访问k节点，代替used数组,保存即将访问却未访问的节点，
        # 弹出的是可以被访问的最小的节点，pop的复杂度是O（1），heappush复杂度log（m）
        q = [(0, k - 1)]
        # 当所有节点都被访问到或者只剩下不连通的节点的时候，堆就为空了，循环终止
        while q:
            # 当前距离最短的终节点
            d, x = heapq.heappop(q)
            print(dist,x,d)
            # 遍历它的相邻节点，如果距离可以被更新，则更新，并被放入到最小堆中
            for y, time in g[x]:
                if (d := dist[x] + time) < dist[y]:
                    dist[y] = d
                    heapq.heappush(q, (d, y))

        ans = max(dist)
        return ans if ans < float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
s1 = Solution()
answer = s1.networkDelayTime(times,n,k)
print(answer)