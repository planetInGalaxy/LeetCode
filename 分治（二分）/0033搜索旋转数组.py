'''
Description: 
Author: Tjg
Date: 2021-10-20 17:50:11
LastEditTime: 2021-10-20 19:11:52
LastEditors: Please set LastEditors
'''
# 二分 官方题解
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 先判断mid在第一组还是第二组中
            # =号不可以去,保证在只有两个数的情况，进入第一组分支
            # 如果已经是有序数组，总是进入第一组
            if nums[0] <= nums[mid]:
                # 判断target是否在从0到mid组成的有序数组中，是则组正常二分
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                # 不是则说明target在右边
                else:
                    l = mid + 1
            # mid在第二组
            else:
                # 判断target是否在从mid到n - 1组成的有序数组中，是则正常二分
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                # 不是则树后面target在mid左边
                else:
                    r = mid - 1
            print(mid,l,r)
        return -1

# 两个数的情况
nums = [3,1]
target = 1
s1 = Solution()
ans = s1.search(nums, target)
print(ans)
