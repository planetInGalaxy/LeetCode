'''
Description: 
Author: Tjg
Date: 2021-07-17 20:05:57
LastEditTime: 2021-08-27 16:03:49
LastEditors: Please set LastEditors
'''



class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 递归法
class Solution:
    def preorder(self, root: 'Node') -> list[int]:
            def preorder(root):
                if root == None:
                    return
                answer.append(root.val)
                for i in root.children:
                    preorder(i)

            answer = []
            preorder(root)
            return answer

# 迭代法
class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if root == None:
            return []
        answer = []
        stack = [root,]
        while stack:
            node = stack.pop()
            answer.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])

        return answer
        
s1 = Solution()
t1 = Node(1)
t1.children = [Node(2)]
answer = s1.preorder(t1)
print(answer)