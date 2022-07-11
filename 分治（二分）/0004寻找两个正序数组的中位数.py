'''
Description: 
Author: Tjg
Date: 2021-06-29 15:08:38
LastEditTime: 2021-06-29 16:20:28
LastEditors: Please set LastEditors
'''
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 
            pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 
            共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 
            共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 
            pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 
            都不可能是第 k 小的元素。把这些元素全部 "删除"，
            剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 
            都不可能是第 k 小的元素。把这些元素全部 "删除"，
            剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），
            因此需要修改 k 的值，减去删除的数的个数
            """
            index1 = index2 = 0
            while True:
                print('k:{} i1:{} i2:{}'.format(k,index1,index2))
                print(nums1[index1:])
                print(nums2[index2:])
                if index1 == len(nums1):
                    return nums2[index2 + k - 1]
                elif index2 == len(nums2):
                    return nums1[index1 + k - 1]
                elif k == 1:
                    return min(nums1[index1], nums2[index2])

                newIndex1 = min(index1 + k // 2 - 1, len(nums1) - 1)
                newIndex2 = min(index2 + k // 2 -1, len(nums2) - 1)


                pivot1 = nums1[newIndex1]
                pivot2 = nums2[newIndex2]
                if pivot1 < pivot2:
                    k -= newIndex1 -index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1


        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (getKthElement(length // 2) + getKthElement(length // 2 + 1)) / 2
        else:
            return getKthElement(length // 2 + 1)

s1 = Solution()
nums1 = [1,3,5,7]
nums2 = [2,4,6,8]
answer = s1.findMedianSortedArrays(nums1,nums2)
print(answer)