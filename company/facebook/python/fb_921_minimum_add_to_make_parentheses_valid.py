"""
- Stack
- Iterate left to right
- When open increment, when close decrement
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = balance = 0

        for c in s:

            balance += 1 if c == '(' else - 1

            # If balance becomes -1, add '(' to make it valid
            # This operation increments answer and recover balance
            if balance == -1:
                ans += 1
                balance += 1

        # print(f'ans: {ans}, balance: {balance}')

        # ans is positive when adding '(' to make it valid
        # balance is positive when there are '(' (so need to add ')')
        return ans + balance


if __name__ == '__main__':
    s = '))'
    s = "())"
    # 1
    s = "((("
    # 3
    print(Solution().minAddToMakeValid(s))
