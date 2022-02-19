'''
Description: 
Author: Tjg
Date: 2022-02-18 00:22:20
LastEditTime: 2022-02-18 00:37:01
LastEditors: Please set LastEditors
'''
# 桶排序
# 时间复杂度O(n+k) 空间复杂度O(n+k)
# 相关 347
class Solution:
    def frequencySort(self, s: str) -> str:
        if s is None or s == "":
            return ""
        

        map = {}
        for i in s:
            map[i] = map.get(i, 0) + 1
        
        min_freq = min(list(map.values()))
        max_freq = max(list(map.values()))
        n = max_freq - min_freq + 1
        sort = [None] * n
        for key, value in map.items():
            if sort[value - min_freq] is None:
                sort[value - min_freq] = []
            sort[value - min_freq].append(key)

        ans = []
        for i in range(n - 1, -1, -1):
            if sort[i] is not None:
                for char in sort[i]:
                    for j in range(i + min_freq):
                        ans.append(char)
                    
        return "".join(ans)
        