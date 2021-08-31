'''
Description: 
Author: Tjg
Date: 2021-08-05 21:26:47
LastEditTime: 2021-08-05 22:09:24
LastEditors: Please set LastEditors
'''
# dfs + 三色
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # 创建三色数组 白：未访问 灰：已访问，不安全 黑：已访问，安全
        color = [0] * len(graph)
        
        def safe(x: int) -> bool:
            # 如果不判断是否已被访问，则会死循环
            if color[x] > 0:
                # 灰色的说明有环，黑色无环
                return color[x] == 2
            # 正在访问，先设为灰色
            color[x] = 1
            # 对邻接的节点进行访问，如果在环内，一定会绕回来，或者有某个节点通向环，返回False
            for y in graph[x]:
                # 如果指向的某个节点有环，则它一定不安全
                if not safe(y):
                    return False
            # 没遇到灰色节点（环或通向环），则设为黑色（安全的）
            color[x] = 2
            return True
        # 遍历所有节点
        return [i for i in range(len(graph)) if safe(i)]
