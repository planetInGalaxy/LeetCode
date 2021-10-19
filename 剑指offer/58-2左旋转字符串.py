'''
Description: 
Author: Tjg
Date: 2021-10-17 15:28:50
LastEditTime: 2021-10-17 15:40:50
LastEditors: Please set LastEditors
'''
# 通过切片把字符串分为两半 再调转顺序拼接起来
# 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if s == "":
            return None

        # 切片形式，如果下标是溢出或者不符合要求，直接返回 []
        # 如果部分满足， 返回满足要求的那部分
        # 索引形式， 如果下标溢出，会报错
        left = s[:n % len(s)]
        right = s[n % len(s):]

        newStr = right + left
        return newStr

s = "ht"
s1 = Solution()
ans = s1.reverseLeftWords(s, 2)
print(ans)