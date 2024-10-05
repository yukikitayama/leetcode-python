from typing import List
import bisect


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # +1 for convenience
        m = max(instructions) + 1
        tree = [0] * (2 * m)

        def update(index, value):
            index += m
            tree[index] += value
            while index > 1:
                index >>= 1
                tree[index] = tree[index << 1] + tree[(index << 1) + 1]

        def query(left, right):
            res = 0
            left += m
            right += m
            while left < right:

                if left & 1:
                    res += tree[left]
                    left += 1
                left >>= 1

                if right & 1:
                    right -= 1
                    res += tree[right]
                right >>= 1

            return res

        ans = 0

        for x in instructions:
            left_cost = query(0, x)
            right_cost = query(x + 1, m)
            ans += min(left_cost, right_cost)
            update(x, 1)

        return ans % MOD

    def createSortedArray1(self, instructions: List[int]) -> int:
        """Naive, T: O(NNlogN)"""
        ans = 0
        nums = []

        for inst in instructions:

            if not nums:
                nums.append(inst)

            else:
                left = bisect.bisect_left(nums, inst)
                right = bisect.bisect_right(nums, inst)
                right = len(nums) - right

                ans += min(left, right)

                nums.append(inst)
                nums.sort()

        return ans