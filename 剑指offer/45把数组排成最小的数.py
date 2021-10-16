'''
Description: 
Author: Tjg
Date: 2021-10-15 16:34:50
LastEditTime: 2021-10-15 17:39:21
LastEditors: Please set LastEditors
'''


# 按照字符串大小的方式进行比较 比较规则： 30 < 3 = 33 < 34
# p228
# 时间复杂度O（nlogn） 空间复杂度O(n)

#1 sort函数 根据经验延展数字串
class Solution:
    def minNumber(self, nums: list[int]) -> str:
        def compare(x):
            x = list(x)
            # 经验值
            x = x * 3
            x = x * ((2 ** 31 - 1) // len(x) + 1)
            x = str(x)
            print(x)
            return (x)

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key = compare)

        return "".join(nums)

#2 快排 比较完备
class Solution:
    def minNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            index = 0
            while True:
                if a[index] <  b[index]:
                    return -1
                elif a[index] > b[index]:
                    return 1
                else:
                    if index == len(a) - 1 and index == len(b) - 1:
                        return 0
                    elif index == len(a) - 1:
                        return compare(b, b[index + 1:] + a)
                    elif index == len(b) - 1:
                        return compare(a[index + 1:] + b, a)
                    else:
                        pass
                index += 1

        def partition(l,r):
            i = l
            j = r
            key = nums[l]
            while i < j:
                while i < j and compare(key, nums[j]) < 0:
                    j -= 1
                while i < j and compare(key, nums[i]) >= 0:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j
        
        def quickSort(l,r):
            if l >= r:
                return
            mid = partition(l,r)
            quickSort(l, mid - 1)
            quickSort(mid + 1, r)

        nums=list(map(str,nums))
        quickSort(0, len(nums) - 1)
        return "".join(nums)


ls = [121,12]
s1 = Solution()
ans = s1.minNumber(ls)
print(ans)