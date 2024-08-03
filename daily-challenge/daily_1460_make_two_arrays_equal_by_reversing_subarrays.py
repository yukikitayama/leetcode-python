from typing import List
import collections


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = collections.Counter(target)
        for num in arr:
            if num not in counter:
                return False
            else:
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
        return True

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)