from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        curr = 0
        for d in derived:
            curr = curr ^ d
        return curr == 0

    def doesValidArrayExist1(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        res0 = original[0] == original[-1]

        original = [1]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        res1 = original[0] == original[-1]

        return res0 or res1