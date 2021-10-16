'''
Description: 
Author: Tjg
Date: 2021-10-16 15:33:37
LastEditTime: 2021-10-16 17:20:28
LastEditors: Please set LastEditors
'''
# 先排序 后统计错位信息 未完成
# 时间复杂度O(nlogn) 空间复杂度O(n)


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        if nums == [] or len(nums) == 1:
            return 0

        numsOrder = sorted(nums)
        counted = set()
        indexMap = {}
        for i in range(len(nums)):
            # if indexMap.get(nums[i], False) == False:
            if nums[i] not in indexMap:
                indexMap[nums[i]] = [i]
            else:
                indexMap[nums[i]].append(i)
        print(indexMap)
        print(numsOrder)

        sum = 0
        for i in range(len(numsOrder)):
            if numsOrder[i] != nums[i] and numsOrder[i] not in counted:
                counted.add(nums[i])

                indexs = indexMap[numsOrder[i]]
                print(indexs)
                for j in indexs:
                    if i < j:
                        break
                print(i, j)
                sum += 2 * (j - i - 1) + 1
                print(sum)

        return sum

# 归并排序统计逆序对
# 时间复杂度O(nlogn) 空间复杂度O(nlogn)
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge(l, r):
            mid = l + (r - l) // 2
            i = mid
            j = r

            for k in range(l, r + 1):
                helper[k] = nums[k]
            # print(l, mid, r, i, j, k,nums, helper)
            nonlocal sum
            for k in range(r, l - 1, -1):
                if i < l:
                    nums[k] = helper[j]
                    j -= 1
                elif j <= mid:
                    nums[k] = helper[i]
                    i -= 1
                elif helper[i] > helper[j]:
                    nums[k] = helper[i]
                    sum += j - mid
                    i -= 1
                else:
                    nums[k] = helper[j]
                    j -= 1


        def mergeSort(l, r):
            if l >= r:
                return
            mid = l + (r - l) // 2
            mergeSort(l, mid)
            mergeSort(mid + 1, r)
            merge(l, r)

        if nums == [] or len(nums) == 1:
            return 0

        sum = 0
        helper = [0] * len(nums)
        mergeSort(0, len(nums) - 1)
        return sum


s1 = Solution()
nums = [1,3,2,3,1]
ans = s1.reversePairs(nums)
print(ans)
