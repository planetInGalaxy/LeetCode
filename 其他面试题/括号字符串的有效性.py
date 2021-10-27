'''
Description: 
Author: Tjg
Date: 2021-08-22 08:08:54
LastEditTime: 2021-08-22 09:08:47
LastEditors: Please set LastEditors
'''
s = input()
brackets_count = 0
for i in s:
    if i != '(' and i != ')':
        print('NO')
        break
    if i == '(':
        brackets_count += 1
    if i == ')':
        brackets_count -= 1
        if brackets_count < 0:
            print('NO')
            break
else:
    if brackets_count == 0:
        print('YES')
    else:
        print('NO')


    