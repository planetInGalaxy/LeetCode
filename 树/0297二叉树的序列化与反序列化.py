'''
Description: 
序列化是将一个数据结构或者对象转换为连续的比特位的操作，
进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，
采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串
并且将这个字符串反序列化为原始的树结构。
Author: Tjg
Date: 2022-02-23 21:57:02
LastEditTime: 2022-02-23 22:48:17
LastEditors: Please set LastEditors
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        traversal_pre = []
        traversal_in = []
        traversal_post = []
        self.preorderTraversal(self,traversal_pre)
        self.inorderTraversal(self,traversal_in)
        self.postorderTraversal(self,traversal_post)
        return "->".join((str(i) for i in traversal_pre)) \
        + '\n' + "->".join((str(i) for i in traversal_in)) \
        + '\n' + "->".join((str(i) for i in traversal_post))

    # 前序遍历
    def preorderTraversal(self, root,traversal):
        if root == None:
            return 
        traversal.append(root.val)
        self.preorderTraversal(root.left,traversal)
        self.preorderTraversal(root.right,traversal)

    # 中序遍历
    def inorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.inorderTraversal(root.left,traversal)
        traversal.append(root.val)
        self.inorderTraversal(root.right,traversal)

    # 后序遍历
    def postorderTraversal(self, root,traversal):
        if root == None:
            return 
        self.postorderTraversal(root.left,traversal)
        self.postorderTraversal(root.right,traversal)
        traversal.append(root.val)

# 前序遍历  注意None的用法
# 时间复杂度O(n) 空间复杂度O(n)
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def preinorder(root):
            if root is None:
                ans.append("None")
                return

            ans.append(str(root.val))
            preinorder(root.left)
            preinorder(root.right)
        
        if root is None:
            return "[]"

        ans = []
        preinorder(root)
        return "[" + ",".join(ans) + "]"
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def preorder():
            nonlocal i
            if data[i] is None:
                i += 1
                return None
            
            root = TreeNode(data[i])
            i += 1
            root.left = preorder()
            root.right = preorder()

            return root

        data =  eval(data)
        if data == []:
            return None
        i = 0
        return preorder()

        

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ser = Codec()
deser = Codec()
data = ser.serialize(root)
print(data)
ans = deser.deserialize(data)
print(ans)