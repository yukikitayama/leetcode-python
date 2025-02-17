"""
dp
backtracking
  hashmap
    k: char, v: count
"""

import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = collections.Counter(tiles)

        def backtracking(counter):

            ans = 0

            for k, v in counter.items():

                if v == 0:
                    continue

                ans += 1
                counter[k] -= 1
                ans += backtracking(counter)
                counter[k] += 1

            return ans

        return backtracking(counter)
