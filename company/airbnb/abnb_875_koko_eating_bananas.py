"""
Example 1
piles: [3, 6, 7, 11], h: 8, output: 4
spends 1 hours to eat the first pile,
spends 2 hour to finish the second pile,
spend 2 hours to finish the third pile,
spends 3 hours to finish the fourth pile

if k is 3,
1 hour for pile[0],
2 hours for pile[1],
3 hours for pile[2],
4 hours for pile[3]
In total, 10 hours, guard comes back before that because of h: 8

Example 2.
piles: [30, 11, 23, 4, 20], h: 5, output: 30
1 hour for pile[0]
1 hour for pile[1]
1 hour for pile[2]
1 hour for pile[3]
1 hour for pile[4]
5 hours in total

Example 3.
piles: [30, 11, 23, 4, 20], h: 6, output: 23
2 hours for piles[0]
1 hour for piles[1]
1 hours for piles[2]
1 hour for piles[3]
1 hour for piles[4]
6 hours in total


Idea
- Greedy?
"""


from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def possible(k):
            # For each pile (p), calculate how many hours take to eat all ((p-1) / k + 1)
            # and calculate total hours from each pile (sum()).
            # If the total hour is less than or equal to h, it's possible for Koko to eat all
            # (p - 1) because otherwise p = k does not work
            # e.g. p: 2, k: 2, hours to spend should be 1
            # but p // k + 1 is 2, and (p - 1) // k + 1 is 1
            return sum((p - 1) // k + 1 for p in piles) <= h

        # Slow eating
        # lo is less than or equal to the answer
        lo = 1
        # Fast eating
        hi = max(piles)

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi

        return lo


"""
Time is O(nlogm) by n piles length and m max value in pile
"""


# p = 30
# p = 11
# p = 23
# p = 4
# p = 24
p = 2
k = 2
# k = 23
print((p - 1) // k + 1)
print(p // k + 1)

piles = [3,6,7,11]
h = 8
piles = [30,11,23,4,20]
h = 5
piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))
