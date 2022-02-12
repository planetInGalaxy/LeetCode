'''
Description: 
Author: Tjg
Date: 2022-02-12 11:16:10
LastEditTime: 2022-02-12 16:59:25
LastEditors: Please set LastEditors
'''
# 贪心 哈希 排序
# 时间复杂度 n = len(task_counts)  m = len(tasks) (n < m)
# sort : O(nlogn) * O(m/n)
# pop : O(n2)
# task_counts[i]-- : O(m)
# O(mlogn + n2)
# 空间复杂度O(n)
import collections
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if tasks is None or tasks == []:
            return 0
        if n == 0:
            return len(tasks)

        freq = collections.Counter(tasks)
        task_counts = list(freq.values())
        ans = 0
        div = 0

        while task_counts != []:
            task_counts.sort(reverse=True)
            print(task_counts)
            if len(task_counts) > n:
                ans += n + 1
                i = 0
                m = n + 1
                while i < m:
                    task_counts[i] -= 1
                    if task_counts[i] == 0:
                        task_counts.pop(i)
                        m -= 1
                    else:
                        i += 1
            else:
                ans += len(task_counts) + div
                div = n - len(task_counts) + 1
                i = 0
                m = len(task_counts)
                while i < m:
                    task_counts[i] -= 1
                    if task_counts[i] == 0:
                        task_counts.pop(i)
                        m -= 1
                    else:
                        i += 1
        
        return ans

# 官方 贪心
# 时间复杂度O(m + n)=O(m)
# 空间复杂度O(n)
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        # 我们首先考虑所有任务种类中执行次数最多的那一种，
        # 记它为A，记执行次数为maxExec。
        # 我们使用一个宽为n+1的矩阵可视化地展现执行A的时间点。
        # 其中任务以行优先的顺序执行，没有任务的格子对应CPU的待命状态。
        # 由于冷却时间为n，因此我们将所有的A排布在矩阵的第一列，满足题意。
        # 同理，如果还有其它也需要执行maxExec次的任务，
        # 我们也需要将它们依次排布成列。例如，当还有任务B和C时，
        # 我们需要将它们排布在矩阵的第二、三列。

        # 如果列数超过了 n+1，那么就算没有待命状态，
        # 任意两个相邻任务的执行间隔肯定也会至少为 n。
        # 此时，总执行时间就是任务的总数|task|。

        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))



tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2

s1 = Solution()
ans = s1.leastInterval(tasks, n)
print(ans)