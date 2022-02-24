'''
Description: 
你这个学期必须选修 numCourses 门课程，
记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 
先修课程按数组 prerequisites 给出，
其中 prerequisites[i] = [ai, bi] ，
表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：
想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？
如果可以，返回 true ；否则，返回 false 。
Author: Tjg
Date: 2022-02-24 20:33:33
LastEditTime: 2022-02-24 20:33:34
LastEditors: Please set LastEditors
'''
# dfs + 三色标记法
# 时间复杂度O(n+m) 空间复杂度O(n+m)
# 图的遍历 时间复杂度为：节点数+边数
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if color[i] == 1:
                return False
            elif color[i] == 2:
                return True
            
            for node in graph[i]:
                color[i] = 1
                ans = dfs(node)
                color[i] = 0
                if ans is False:
                    return False
            
            color[i] = 2
            return True

        if numCourses <= 0 or prerequisites is None:
            return None
        if prerequisites == []:
            return True
        
        # 邻接表 空间复杂度O(n+m)
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
        

        # 用于判断在本次路径搜索中，
        # 当前到达的节点之前是否已经访问过（1），
        # 即当前路径是否有环，
        # 以及判断该节点是是否已经被完全搜索过（2）
        color = [0] * numCourses
        ans = True
        for i in range(numCourses):
            if graph[i] != [] and color[i] != 2:
                ans = dfs(i)
                if ans is False:
                    return False
        else:
            return True