'''
Description: 
Author: Tjg
Date: 2021-07-27 14:33:24
LastEditTime: 2021-07-27 14:56:38
LastEditors: 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 不没有用到题目条件
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def traverse(root):
            nums = []
            nums.append(root.val)
            if root.left:            
                nums_left = traverse(root.left)
                merge(nums,nums_left)
            if root.right:
                nums_right = traverse(root.right)
                merge(nums,nums_right)
            # print(nums)
            return nums

        def merge(nums,sub_nums):
            for i in sub_nums:
                if len(nums) == 1:
                    if i < nums[0]:
                        nums.insert(0,i)
                    elif i > nums[0]:
                        nums.append(i)
                    else:
                        pass
                else:
                    for j in range(len(nums)):
                        if i < nums[j]:
                            nums.insert(j,i)
                            nums.pop()
                            break
                        if i == nums[j]:
                            break
        nums = traverse(root)
        if len(nums) < 2:
            return - 1
        else:
            return nums[1]
# 官方 
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans, rootvalue = -1, root.val

        def dfs(node: TreeNode) -> None:
            nonlocal ans
            if not node:
                return
            if ans != -1 and node.val >= ans:
                return # 根据题目条件 剪枝
            if node.val > rootvalue:
                ans = node.val
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

s1 =Solution()
t1 = TreeNode(5)
t1.left = TreeNode(8)
t1.right = TreeNode(5)
answer = s1.findSecondMinimumValue(t1)
print(answer)