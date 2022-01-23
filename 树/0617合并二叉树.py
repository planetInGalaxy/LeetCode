'''
Description: 
Author: Tjg
Date: 2022-01-09 17:07:25
LastEditTime: 2022-01-09 17:26:43
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 前序遍历
# 当前的两个节点一定不为空，所以先更新val
# 判断两个节点拥有左子节点的情况和拥有右子节点的情况
# 如果都有，则前序遍历出来两个节点的左（右）子节点
# 如果root1树没有，则将root2对应的子节点添加上去
# 其余情况不用处理
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def preOrderTravel(node1, node2):
            node1.val += node2.val
            if node1.left and node2.left:
                preOrderTravel(node1.left, node2.left)
            elif node1.left is None:
                node1.left = node2.left
            if node1.right and node2.right:
                preOrderTravel(node1.right, node2.right)
            elif node1.right is None:
                node1.right = node2.right
            return

        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            preOrderTravel(root1, root2)
            return root1
            