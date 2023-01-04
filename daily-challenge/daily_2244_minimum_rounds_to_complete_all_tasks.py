"""
- Greedy
- Heap
"""


from typing import List
import collections


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        counter = collections.Counter(tasks)

        ans = 0

        for k, v in counter.items():

            if v == 1:
                return -1

            if v % 3 == 0:
                ans += v // 3

            # v == 4, 2 and 2
            # v == 2, 2
            elif v % 3 == 1:
                ans += v // 3 + 1

            # v == 5, 3 and 2
            elif v % 3 == 2:
                ans += v // 3 + 1

        return ans


if __name__ == '__main__':
    tasks = [2,2,3,3,2,4,4,4,4,4]
    # 4
    # tasks = [2, 3, 3]
    # -1
    # tasks = [5, 5, 5, 5]
    # 2
    print(Solution().minimumRounds(tasks))


