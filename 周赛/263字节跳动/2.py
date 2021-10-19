'''
Description: 
Author: Tjg
Date: 2021-10-17 10:39:18
LastEditTime: 2021-10-17 10:52:44
LastEditors: Please set LastEditors
'''
class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= self.n and account2 <= self.n \
            and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False 

    def deposit(self, account: int, money: int) -> bool:
        if account <= self.n:
            self.balance[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.n and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:

balance = [10, 100, 20, 50, 30]
bank = Bank(balance)
ans = []
ans.append(bank.withdraw(3, 10))
ans.append(bank.transfer(5, 1, 20))
ans.append(bank.deposit(5, 20))
ans.append(bank.transfer(3, 4, 15))
ans.append(bank.withdraw(10, 50))
print(ans)