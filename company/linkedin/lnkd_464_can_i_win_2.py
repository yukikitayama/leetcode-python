"""
- https://leetcode.com/problems/can-i-win/discuss/159797/Python-98.5-simple-READABLE-code-with-good-comments
- Sum of integers from 1 to n
  - https://www.wikihow.com/Sum-the-Integers-from-1-to-N
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # ?
        seen = {}

        def can_win(choices, remainder):

            # If the largest number is bigger than remaining, the first person
            # can pick it, and wins
            if choices[-1] >= remainder:
                return True

            seen_key = tuple(choices)

            # print(f'  seen_key: {seen_key}')

            if seen_key in seen:
                return seen[seen_key]

            for index in range(len(choices)):

                if not can_win(
                    choices[:index] + choices[index + 1:],
                    remainder - choices[index]
                ):
                    seen[seen_key] = True
                    return True

            seen[seen_key] = False

            return False

        # Sum of consecutive integers from 1 to n: (n(n + 1))/2
        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2

        # If the sum of integers from 1 to n is smaller than desiredTotal
        # first person cannot reach desiredTotal
        if summed_choices < desiredTotal:
            return False

        # If sum of integers from 1 to n is equal to desiredTotal,
        # then the first person can win if the number of total turn is odd
        # Meaning at the last turn is First if it's odd, and it reaches desiredTotal,
        # and the first person wins
        # maxChoosableInteger: 3, 3 % 2: 1, 1: True
        # maxChoosableInteger: 4, 4 % 2: 0, 0: False
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2

        choices = list(range(1, maxChoosableInteger + 1))

        # print(f'choices: {choices}')

        return can_win(choices, desiredTotal)


# False
maxChoosableInteger = 10
desiredTotal = 11
# True
maxChoosableInteger = 10
desiredTotal = 0
# True
maxChoosableInteger = 10
desiredTotal = 1
maxChoosableInteger = 10
desiredTotal = 50
print(Solution().canIWin(maxChoosableInteger, desiredTotal))

