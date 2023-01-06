"""
- sort or min heap
"""


from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        # Counting sort
        m = max(costs)
        # +1 because 0 index won't be used
        array = [0] * (m + 1)
        for cost in costs:
            array[cost] += 1

        ans = 0

        for cost in range(len(array)):

            if array[cost] == 0:
                continue

            elif cost > coins:
                break

            else:
                # Pick all or minimum count by remaining coins
                count = min(array[cost], coins // cost)

                ans += count

                coins -= cost * count

        return ans


if __name__ == '__main__':
    costs = [1, 3, 2, 4, 1]
    coins = 7
    print(Solution().maxIceCream(costs, coins))
