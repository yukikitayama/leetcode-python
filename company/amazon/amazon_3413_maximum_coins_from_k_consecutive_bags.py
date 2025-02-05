"""
Interval starts at left or starts at right
One sliding window to check the interval starting at left
One sliding window to check the interval ending at left

cur is the coins from k consecutive bags
part?
"""

from typing import List


class Solution:
    def maximumCoins1(self, coins: List[List[int]], k: int) -> int:
        def slide(A):
            A.sort()
            res = cur = j = 0
            for i in range(len(A)):
                cur += (A[i][1] - A[i][0] + 1) * A[i][2]
                while A[j][1] < A[i][1] - k + 1:
                    cur -= (A[j][1] - A[j][0] + 1) * A[j][2]
                    j += 1
                part = max(0, A[i][1] - k - A[j][0] + 1) * A[j][2]
                res = max(res, cur - part)
            return res

        return max(slide(coins), slide([[-r, -l, w] for l, r, w in coins]))

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:

        ans = 0

        # Sort coins by interval start and end
        coins.sort()
        # print(coins)

        cur = 0

        # Sliding window left
        left = 0
        # Sliding window right
        for right in range(len(coins)):

            # Length * unit coin
            cur += (coins[right][1] - coins[right][0] + 1) * coins[right][2]

            # k: 3 [1, 2, X], [5, 6, X], 6 - 3 + 1 = 4
            # LHS: previous interval right
            # RHS: interval left end with size k
            # If <, no overlap. Need to shrink sliding window
            while coins[left][1] < coins[right][1] - k + 1:
                # Remove coins gained by previous interval
                # Length * unit coin
                cur -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]
                left += 1

            # When window spans multiple intervals, need to subtract where window and previous interval don't overlap
            # [1, 3, 2], [5, 6, 4], k: 4, window: [3, 6], need to subtract: [1, 2]
            # 6 - 4 - 1 + 1 = 2
            # coins[right][1] - k: right index after subtracting window,
            # coins[left][0]: left index of the interval to subtract
            # +1 for being inclusive
            subtract_length = max(
                0,
                ((coins[right][1] - k) - coins[left][0] + 1)
            )
            subtract = subtract_length * coins[left][2]

            ans = max(ans, cur - subtract)

            # print(f"ans: {ans}, cur: {cur}, left: {left}, right: {right}")

        # [l, r, c] -> [-r, -l, c]
        # [1, 3, 2] -> [-3, -1, 2]

        coins = [[-r, -l, c] for l, r, c in coins]
        coins.sort()

        cur = 0

        # Sliding window left
        left = 0
        # Sliding window right
        for right in range(len(coins)):

            # Length * unit coin
            cur += (coins[right][1] - coins[right][0] + 1) * coins[right][2]

            # k: 3 [1, 2, X], [5, 6, X], 6 - 3 + 1 = 4
            # LHS: previous interval right
            # RHS: interval left end with size k
            # If <, no overlap. Need to shrink sliding window
            while coins[left][1] < coins[right][1] - k + 1:
                # Remove coins gained by previous interval
                # Length * unit coin
                cur -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]
                left += 1

            # When window spans multiple intervals, need to subtract where window and previous interval don't overlap
            # [1, 3, 2], [5, 6, 4], k: 4, window: [3, 6], need to subtract: [1, 2]
            # 6 - 4 - 1 + 1 = 2
            # coins[right][1] - k: right index after subtracting window,
            # coins[left][0]: left index of the interval to subtract
            # +1 for being inclusive
            subtract_length = max(
                0,
                ((coins[right][1] - k) - coins[left][0] + 1)
            )
            subtract = subtract_length * coins[left][2]

            ans = max(ans, cur - subtract)

            # print(f"ans: {ans}, cur: {cur}, left: {left}, right: {right}")

        return ans