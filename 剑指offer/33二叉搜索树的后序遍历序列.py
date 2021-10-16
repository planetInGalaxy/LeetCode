'''
Description: 
Author: Tjg
Date: 2021-10-10 09:57:50
LastEditTime: 2021-10-10 10:24:29
LastEditors: Please set LastEditors
'''
# 时间复杂度O(n) 空间复杂度 最好O(logn) 最坏O(n)
class Solution:
    def verifyPostorder(self, postorder: list[int]) -> bool:
        def verify(start, end):
            if start >= end:
                return True
            # print(start, end)
            root = postorder[end]
            right_start = start

            while right_start < end and postorder[right_start] < root:
                right_start += 1
            
            right_pointer = right_start
            while right_pointer < end:
                if postorder[right_pointer] < root:
                    return False
                right_pointer += 1
            
            return verify(start, right_start - 1) and \
                verify(right_start, end - 1)
        

        if postorder == []:
            return True
        
        return verify(0, len(postorder) - 1)


tree = [1,3,2,6,5]
s1 = Solution()
ans = s1.verifyPostorder(tree)
print(ans)
        