"""
- https://leetcode.com/problems/can-i-win/discuss/95277/Java-solution-using-HashMap-with-detailed-explanation
- TLE
"""


class Solution:
    def __init__(self):
        self.map = None
        self.used = None

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # ?
        sum = (1 + maxChoosableInteger) * maxChoosableInteger / 2

        # print(f'sum: {sum}')

        if sum < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True

        self.map = {}
        self.used = [False] * (maxChoosableInteger + 1)

        # print(f'used: {self.used}')

        return self.helper(desiredTotal)

    def helper(self, desiredTotal):
        if desiredTotal <= 0:
            return False

        # Key is an integer representing which integers from 1 to maxChoosableInteger are used
        # If key is 7, bin(7) is '0b111', integers 1, 2, 3 are used
        key = self.format(self.used)

        # print(f'  key: {key}')

        if key not in self.map:

            for i in range(1, len(self.used)):

                if not self.used[i]:
                    self.used[i] = True

                    if not self.helper(desiredTotal - i):
                        self.map[key] = True
                        self.used[i] = False
                        return True

                    self.used[i] = False

            self.map[key] = False

        return self.map[key]

    def format(self, used):
        # To see bit representation, bin(num)
        # e.g. used = [True, True], bin(num): '0b11', num: 3
        # e.g. used = [True, True, True], bin(num): '0b111', num: 7
        num = 0
        for b in self.used:
            num <<= 1
            if b:
                num |= 1

        return num


# False
maxChoosableInteger = 10
desiredTotal = 11
# True
maxChoosableInteger = 10
desiredTotal = 0
# True
maxChoosableInteger = 10
desiredTotal = 1
print(Solution().canIWin(maxChoosableInteger, desiredTotal))

