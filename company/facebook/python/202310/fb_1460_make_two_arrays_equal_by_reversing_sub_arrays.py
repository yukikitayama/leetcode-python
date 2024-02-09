"""
- Distinct?
- Compare hashmap?
"""


from typing import List
import collections


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Equality compare corresponding counts
        return collections.Counter(target) == collections.Counter(arr)


if __name__ == '__main__':
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(Solution().canBeEqual(target, arr))
