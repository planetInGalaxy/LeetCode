'''
Description: 
Author: Tjg
Date: 2021-11-14 11:01:40
LastEditTime: 2021-11-14 11:33:40
LastEditors: Please set LastEditors
'''
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == "":
            return ""
            
        cols = len(encodedText) // rows
        # print(cols)
        strings = [encodedText[i * cols : (i + 1) *cols] for i in range(rows)]
        # print(strings)
        result = []
        for i in range(cols):
            for j in range(rows):
                if j < rows and j + i < cols:
                    result.append(strings[j][j+i])
        # print(result)
        while result[-1] == ' ':
            result.pop()
        return "".join(result)


encodedText = " b  ac"
rows = 2
s1 = Solution()
ans = s1.decodeCiphertext(encodedText, rows)
print(ans)