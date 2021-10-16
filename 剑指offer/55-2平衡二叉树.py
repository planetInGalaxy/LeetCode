'''
Description: 
Author: Tjg
Date: 2021-10-16 21:01:37
LastEditTime: 2021-10-16 21:26:51
LastEditors: Please set LastEditors
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# p274
# 借用序列化二叉树的代码 建树
# 后序遍历 先求出两个子树的深度
# 如果某个子树深度为-1 说明子树不为平衡树 返回-1
# 如果都不为-1，求他们的平衡因子是否为+1或-1
# 满足平衡二叉树则返回新树的深度，否则返回-1
# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O(n)
import collections
class Solution:
    def deserialize(self, data):
        if data == "[]":
            return

        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

    def isBalanced(self, root: TreeNode) -> bool:
        def travel(node):
            if node is None:
                return 0

            leftDepth = travel(node.left)
            rightDepth = travel(node.right)
            # print(node.val, leftDepth, rightDepth)
            
            if leftDepth == -1 or rightDepth == -1:
                return -1

            if abs(rightDepth - leftDepth) <= 1:
                return max(leftDepth, rightDepth) + 1
            else:
                return -1
        
        rootDepth = travel(root)

        if rootDepth >= 0:
            return True
        else:
            return False


s1 = Solution()
treeStr = "[1,2,2,3,3,null,null,4,4,null,null,null,null,null,null]"
tree = s1.deserialize(treeStr)
ans = s1.isBalanced(tree)
print(ans)