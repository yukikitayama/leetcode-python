"""
The coefficients in factorial representation are indexes of elements in the input array.
"""

import itertools


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1 because 0! = 1
        factorials = [1]
        nums = ["1"]
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))

        # print(f"factorials: {factorials}")
        # print(f"nums: {nums}")

        k -= 1

        ans = []
        for i in range(len(factorials) - 1, -1, -1):
            # // because of how coefficients in factorial representation increments
            idx = k // factorials[i]

            # // because of how coefficients in factorial representation increments
            k -= idx * factorials[i]

            num = nums[idx]
            ans.append(num)
            del nums[idx]

        return "".join(ans)

    def getPermutation1(self, n: int, k: int) -> str:
        perm = itertools.permutations(range(1, n + 1))
        for p in perm:
            k -= 1
            if k == 0:
                return "".join([str(d) for d in p])
        return ""