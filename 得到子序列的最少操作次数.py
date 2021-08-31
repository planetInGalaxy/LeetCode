'''
Description: 连带1143 300
Author: Tjg
Date: 2021-07-26 11:41:50
LastEditTime: 2021-07-26 14:11:59
LastEditors: Please set LastEditors
'''
# 贪心+二分  1143 最长公共子序列 -> 300 最长递增子序列
import bisect
class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        # 分析:
        # 本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少)
        # 根据target中互不相同，我们知道每个数字对应的坐标唯一
        # 于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列

        # 数字对应坐标
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300.最长上升子序列
        increase = []
        for num in arr:
            # 只有在target的数字才可能属于公共子序列
            if num in idx_dict:
                # 转换坐标
                idx = idx_dict[num]
                # 该坐标在当前栈中的位置
                i = bisect.bisect_left(increase, idx)
                # 如果在最后要加入元素，否则要修改该位置的元素
                # 跟一般的讲，i代表了目前这个idx在increase中的大小位置，
                # 在前面出现还比idx大的increase中的元素是无法和idx构成最长上升子序列的。
                # i左边的数比idx小，可以和idx构成上升子序列，(idx构成的长度就是i+1)
                # idx比i的值小，将i替换后可以方便后面构成更优的子序列(越小后面能加入的数越多)
                if i == len(increase):
                    increase.append(idx)
                else:
                    increase[i] = idx
        # 最终increase的长度就构成了最长上升子序列的长度，用减法即可得到本题答案
        return len(target) - len(increase)


s1 = Solution()

target = [17,5,7,1,2,19,4,20,10,18]
arr = [2,10,5,9,9,17,8,1,19,1]

answer = s1.minOperations(target,arr)
print(answer)