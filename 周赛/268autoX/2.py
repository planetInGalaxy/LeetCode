'''
Description: 
Author: Tjg
Date: 2021-11-21 10:35:32
LastEditTime: 2021-11-21 10:45:25
LastEditors: Please set LastEditors
'''
class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        remain = capacity
        steps = 0
        for i in range(len(plants)):
            if remain >= plants[i]:        
                steps += 1
                remain -= plants[i]
            else:
                steps += 2 * i + 1
                remain = capacity - plants[i]  
        return steps