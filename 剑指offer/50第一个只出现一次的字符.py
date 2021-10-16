'''
Description: 
Author: Tjg
Date: 2021-10-16 12:08:10
LastEditTime: 2021-10-16 12:25:31
LastEditors: Please set LastEditors
'''

# 字典 布尔值
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            # 空： True  True：False  False：False
            dic[c] = c not in dic
        for c in s:
            if dic[c]: 
                return c
        return ' '
        
# 自制哈希表(自制的很慢) p244
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return ' '
        
        hashTable = [0] * 26
        for i in s:
            hashTable[ord(i) - ord('a')] += 1
            # hashTable[ord(i) - ord('a')] = hashTable[ord(i) - ord('a')] is 0
        for i in s:
            if hashTable[ord(i) - ord('a')] == 1:
            # if hashTable[ord(i) - ord('a')] == True:
                return i
        return ' '
        
s = "aad"
s1 = Solution()
ans = s1.firstUniqChar(s)
print(ans)