'''
Description: 因为无环，无需检查当前节点是否遍历过
Author: Tjg
Date: 2021-08-25 19:21:49
LastEditTime: 2021-08-25 22:26:54
LastEditors: Please set LastEditors
'''
# dfs 
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans = []
        path = []
        n = len(graph)
        def dfs(i):
            path.append(i)
            if i == n - 1:
                ans.append(path[:])
                return 

            for j in range(len(graph[i])):
                dfs(graph[i][j])
                path.pop()
            # print(path)
        
        dfs(0)
        # print(ans)
        return ans

graph = [[4,3,1],[3,2,4],[3],[4],[]]
s1 = Solution()
s1.allPathsSourceTarget(graph)