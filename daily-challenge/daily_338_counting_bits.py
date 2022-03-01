from typing import List
import collections


class Solution:
    def countBits(self, n: int) -> List[int]:
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1
                count += 1
            return count

        ans = []
        for x in range(n + 1):
            ans.append(pop_count(x))

        return ans


class Solution1:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(collections.Counter(bin(i)[2:])['1'])
            # print(collections.Counter(bin(i)[2:]))
        return ans


if __name__ == '__main__':
    n = 2
    n = 5
    # [0,1,1,2,1,2]
    print(Solution().countBits(n))
