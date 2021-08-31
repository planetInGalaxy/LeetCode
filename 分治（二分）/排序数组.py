'''
Description: 
Author: Tjg
Date: 2021-08-23 18:04:59
LastEditTime: 2021-08-23 20:55:18
LastEditors: Please set LastEditors
'''



class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def insertSort(arr, l, r):
            for i in range(l + 1, r + 1):
                temp = arr[i]
                for j in range(i, l - 1, -1):
                    if j == 0 or temp >= arr[j - 1]:
                        arr[j] = temp
                        break
                    else:
                        arr[j] = arr[j - 1]
                        
        def partition(arr, l, r):
            i = l
            j = r
            key = arr[l]
            # print(l, r, i, j, key, arr)
            while True:
                while i < j and arr[j] >= key:
                    j -= 1
                # print(j)
                while i < j and arr[i] <= key:
                    i += 1
                # print(i)
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
                # print(j, j, arr)
            # j = i i - 1 或者 i - 2
            arr[j],arr[l] = arr[l], arr[j]
            return j 

        def quickSort(arr, l, r):
            if l + 10 >= r:
                insertSort(arr, l, r)    
                return
            mid = partition(arr, l,r)
            quickSort(arr, l, mid - 1)
            quickSort(arr, mid + 1, r)

        arr = nums
        quickSort(arr, 0, len(arr) - 1)
        return nums




class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def bubbleSort(arr):
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if arr[j + 1] < arr[j]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        return bubbleSort(nums)
