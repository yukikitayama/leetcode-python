"""
s: "abbbba"
a: 2, b: 4, len: 6
exp: 3

Sorting?
Binary search?

"pqqppqpqpq"
"""


class Solution:
    def minAnagramLength(self, s: str) -> int:

        counter = collections.Counter(s)

        left = 0
        right = len(s)

        # mid = (left + right) // 2
        # counter_left = collections.Counter(s[:mid])
        # counter_right = collections.Counter(s[-mid:])
        # print(mid, counter_left, counter_right)

        ans = float("inf")

        while left <= right:

            mid = (left + right) // 2

            counter_left = collections.Counter(s[:mid])
            counter_right = collections.Counter(s[-mid:])

            print(mid, counter_left, counter_right)

            if counter_left == counter_right and len(s) % mid == 0 and counter_left.keys() == counter.keys():
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans