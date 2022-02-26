'''
Description: 
Author: Tjg
Date: 2022-02-24 22:03:02
LastEditTime: 2022-02-25 22:29:34
LastEditors: 
'''
'''
Description: 
Trie(发音类似"try"),或者说：前缀树，是一种树形数据结构，
用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
Trie() :
初始化前缀树对象
void insert(String word) :
向前缀树中插入字符串 word
boolean search(String word) : 
如果字符串 word 在前缀树中，返回 true
(即，在检索之前已经插入)；否则，返回 false
boolean startsWith(String prefix) :
如果之前已经插入的字符串 word 的前缀之一为 prefix
返回 true ；否则，返回 false 
Author: Tjg
Date: 2022-02-24 22:03:02
LastEditTime: 2022-02-24 22:04:44
LastEditors: Please set LastEditors
'''
# 前缀树/字典树
# 是一棵每个节点有m个子节点的树，m是字符种类
# 时间复杂度：
# 初始化 O(m) 其余操作O(len(s))
# 空间复杂度O(m*len(s))
class Trie:
    def __init__(self):
        # 指向子节点的指针列表
        self.children = [None] * 26
        # 表示该节点是否是字符串的末尾
        self.isEnd = False

    # 查找前缀
    # 从根开始查找前缀
    # 子节点存在，指针下移，查找一下一个字符
    # 子节点不存在，说明不存在该前缀，返回空指针
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    # 插入字符串
    # 子节点存在，指针直接下移，处理下一个字符
    # 子节点不存在，新建一个子节点并继续处理
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    # 根据查找到之后返回的节点进行判断
    # 如果不为None，而且是末尾，则说明有该字符串
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    # 根据查找到之后返回的节点进行判断
    # 如果不为None，无论是不是末尾，都说明有该前缀
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


# Your Trie object will be instantiated and called as such:
word = "abc"
prefix = "ab"
obj = Trie()
obj.insert(word)
ans = obj.search(word)
print(ans)
ans = obj.startsWith(prefix)
print(ans)