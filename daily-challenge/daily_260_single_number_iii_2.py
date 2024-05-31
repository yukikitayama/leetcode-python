from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0

        # Filter out twice appearing nums by x^x=0 and a^x^x=a rule
        for num in nums:
            bitmask ^= num

        # 3: 011, 5: 101
        # bitmask: 110
        # -bitmask: 001 + 1 = 010
        # diff: 110 & 010 = 010
        # diff is the rightmost different bit between 011 (3) and 101 (5)
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            # Find a number which has overlap with this diff to extract at least one number
            if num & diff:
                # Cannot simple x = num, becuase twice-appearing numbers can overlap with diff
                # but they appear twice, so XOR twice can filter out those number
                # and can keep once appearing number
                x ^= num

        # bitmask contains x so XOR again to filter out x from bitmask to leave y only
        return [x, bitmask ^ x]

    def singleNumber1(self, nums: List[int]) -> List[int]:
        ans = set()

        for num in nums:

            if num not in ans:
                ans.add(num)
            else:
                ans.discard(num)

        return list(ans)