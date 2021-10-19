'''
Description: 
Author: Tjg
Date: 2021-10-17 11:12:50
LastEditTime: 2021-10-17 11:53:18
LastEditors: Please set LastEditors
'''
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        def dfs(node):
            if node == n - 1:
                pass
            nonlocal currentTime
            for i in edgesMatrix[node]:
                if currentTime // change % 2 == 0:
                    currentTime += time

                pass



        edgesMatrix = [[0] * n] * n
        for i in edges:
            edgesMatrix[i[0]][i[1]] = 1
            edgesMatrix[i[1]][i[0]] = 1
            
        currentTime = 0
        timeSet = set()
        color = [0] * n
        dfs(0)
        minTime = min(timeSet)
        timeSet.remove(minTime)
        return min(timeSet)