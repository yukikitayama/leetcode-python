from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if account1 < 1 or account1 > len(self.balance) or account2 < 1 or account2 > len(self.balance):
            return False

        curr_amount = self.balance[account1 - 1]

        if curr_amount < money:
            return False

        else:
            self.balance[account2 - 1] += money
            self.balance[account1 - 1] -= money
            return True

    def deposit(self, account: int, money: int) -> bool:

        if account < 1 or account > len(self.balance):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:

        if account < 1 or account > len(self.balance):
            return False

        curr_amount = self.balance[account - 1]

        if curr_amount < money:
            return False

        else:
            self.balance[account - 1] = curr_amount - money
            return True


balance = [10, 100, 20, 50, 30]
bank = Bank(balance)
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))