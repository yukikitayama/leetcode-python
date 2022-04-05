"""
- Length is even
- one half is some numbers, the other half is the doubles
"""


from typing import List
import collections


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        count = collections.Counter(changed)

        # print(f'count: {count}')

        for x in sorted(count):

            # count[2]: 2, count[2 * 2 = 4]: 1, no because we don't have enough doubled number
            if count[x] > count[2 * x]:
                return []

            # Use current number to decrement its doubled number count
            # if x because we wanna do something different if x is 0
            # double of 0 is still 0, so if x is 0, directly reduce the number by half
            count[2 * x] -= count[x] if x else count[x] // 2

        # elements() returns iterator so convert it to list
        # elements() repeats the key by value times
        ans = list(count.elements())

        return ans


if __name__ == '__main__':
    changed = [1, 3, 4, 2, 6, 8]
    changed = [6, 3, 0, 1]
    changed = [1]
    changed = [0, 0, 0, 0]
    # [0, 0] because 0 * 2 = 0
    changed = [0]
    print(Solution().findOriginalArray(changed))

    test = {0: 4}
    print(test)
    x = 0
    test[2 * x] -= test[x] if x else test[x] / 2
    print(test)
