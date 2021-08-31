'''
Description: 
Author: Tjg
Date: 2021-08-27 09:16:01
LastEditTime: 2021-08-27 09:42:31
LastEditors: Please set LastEditors
'''
# 先移动 再前向双指针
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 自右向左，逐个移动
        for i in range(m - 1, -1, -1):
            nums1[n + i] = nums1[i]
        i = 0
        ptr1 = n
        ptr2 = 0
        while ptr2 < n:
            if ptr1 < n + m and nums1[ptr1] < nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 += 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 += 1
            i += 1
            # print(nums1)

# 无需移动 后向双指针
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        # while p1 >= 0 or p2 >= 0:
        #     if p1 == -1:
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     elif p2 == -1:
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     elif nums1[p1] > nums2[p2]:
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     tail -= 1
        while  p2 >= 0:
            if p1 >= 0 and nums1[p1]> nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
            # print(nums1)

nums1 = [1,2,4,5,6,0]
nums2 = [3]
m = 5
n = 1
s1 = Solution()
s1.merge(nums1, m, nums2, n)