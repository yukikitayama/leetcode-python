"""
Check if counter key set length is equal to value set length
"""

from typing import List
import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counter = collections.Counter(arr)

        return len(counter.keys()) == len(set(counter.values()))


if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    arr = [1, 2]
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(Solution().uniqueOccurrences(arr))
