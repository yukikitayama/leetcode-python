"""
]]][[[
1, []][[], swap first and last
2. [][][], swap two in the middle

Iteration from left to right doesn't return minimum
Two pointers from left and from right?

If balance is negative, find close from right?
"""


class Solution:
    def minSwaps(self, s: str) -> int:

        left = 0
        right = len(s) - 1

        balance = 0

        buffer = [ch for ch in s]

        ans = 0

        for left in range(len(buffer)):

            if buffer[left] == "[":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                while left < right and buffer[right] != "[":
                    right -= 1
                # Swap
                buffer[left], buffer[right] = buffer[right], buffer[left]
                ans += 1
                # The above creates [ at left, it means we need to rest the balance to be 1 opening bracket
                balance = 1

            # print(left, balance, ans)

        return ans
