'''
Description: 
Author: Tjg
Date: 2021-11-15 06:42:57
LastEditTime: 2021-11-15 07:20:54
LastEditors: Please set LastEditors
'''
# frozenset可以做字典的键
# frozenset存储二元组，可以模拟不可变字典
# 时间复杂度O(m*n) 空间复杂度O(m*n)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}
        for i in strs:
            word = {}
            for j in i:
                word[j] = word.get(j, 0) + 1
            wordSet = frozenset(word.items())
            # print(wordSet)
            if wordSet in words:
                words[wordSet].append(i)
            else:
                words[wordSet] = [i]
        
        result = []
        for i in words.values():
            result.append(i)

        return result

# 官方
# 对每个单词进行排序（异位词排完序后相同），再放到字典中相应的位置
# 时间复杂度O(mlogm*n) 空间复杂度O(m*n)
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

strList = ["ddddddddddg","dgggggggggg"]
s1 = Solution()
ans = s1.groupAnagrams(strList)
print(ans)