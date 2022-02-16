'''
Description: 
给定一个二叉树，编写一个函数来获取这个树的最大宽度。
树的宽度是所有层中的最大宽度。
这个二叉树与满二叉树结构相同，但一些节点为空。
每一层的宽度被定义为两个端点,即该层最左和最右的非空节点，
两端点间的null节点也计入长度之间的长度。
Author: Tjg
Date: 2022-02-16 20:58:49
LastEditTime: 2022-02-16 21:41:05
LastEditors: Please set LastEditors
'''
# BFS
# 时间复杂度O(n) 空间复杂度O(n)
class Solution():
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans

# DFS
# 时间复杂度O(n) 空间复杂度O(n)
class Solution():
    def widthOfBinaryTree(self, root):
        def dfs(root, depth, pos):
            if root is None:
                return
            
            nonlocal ans
            left.setdefault(depth, pos)
            ans = max(ans, pos - left[depth] + 1)
            dfs(root.left, depth+1, pos*2)
            dfs(root.right, depth+1, pos*2+1)

        left = {}
        ans = 0
        
        dfs(root, 0, 0)
        return ans