'''
Description: 
Author: Tjg
Date: 2021-10-24 10:57:29
LastEditTime: 2021-10-24 11:51:40
LastEditors: Please set LastEditors
'''
class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        def countNodes(root):
            if root is None:
                return 0
            if root in subTreeNodes.keys():
                return subTreeNodes[root]
            
            leftCount = countNodes(root.left)
            rightCount = countNodes(root.right)
            
            count = leftCount + rightCount + 1
            subTreeNodes[root] = count
            return count

        subTreeNodes = {}
        for i in parents:
            countNodes(i)
        
        print(subTreeNodes)

class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        def countNodes(n):
            if n not in childrenMap:
                return 1
            
            count = 1
            for i in childrenMap[n]:
                count += countNodes(i)
            countMap[n] = count
            return count

        childrenMap = {}
        for i in range(len(parents)):
            if parents[i] in childrenMap:
                childrenMap[parents[i]].append(i)
            else:
                childrenMap[parents[i]] = [i]

        countMap = {}
        countNodes(-1)

        # print(childrenMap)
        # print(countMap)
        
        resultMap = {} 
        maxResult = 0
        n = len(parents)
        for i in range(n):
            children = childrenMap.get(i, [])
            # print(children,i)
            if children == []:
                result = n - 1
            elif len(children) == 1:
                if i != 0:
                    result = countMap.get(children[0], 1) * (n - 1 - countMap.get(children[0], 1))
                else:
                    result = n - 1
            else:
                if i != 0:
                    result = countMap.get(children[0], 1) * countMap.get(children[1], 1) * \
                        (n - 1 - countMap.get(children[0], 1) - countMap.get(children[1], 1))
                else:
                    result = countMap.get(children[0], 1) * countMap.get(children[1], 1)
                    
            # print(i, result)
            resultMap[result] = resultMap.get(result, 0) + 1
            maxResult = max(maxResult, result)
        
        # print(resultMap)
        return resultMap[maxResult]


parents = [-1,2,0]
s1 = Solution()
ans = s1.countHighestScoreNodes(parents)
print(ans)