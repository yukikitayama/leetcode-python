from typing import List
import collections


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        counter = collections.Counter(changed)

        # print(counter)

        changed.sort()

        ans = []

        for num in changed:

            if num == 0 and counter[num] >= 2:
                ans.append(num)
                counter[num] -= 2
            elif num != 0 and counter[num] > 0 and counter[2 * num] > 0:
                ans.append(num)
                counter[num] -= 1
                counter[2 * num] -= 1

        return ans if len(ans) == len(changed) // 2 else []


if __name__ == '__main__':
    changed = [1, 3, 4, 2, 6, 8]
    # [1, 3, 4]
    # changed = [6, 3, 0, 1]
    # []
    # changed = [1]
    # []
    # changed = [0, 0, 0, 0]
    # [0, 0]
    # changed = [1,2,3,2,4,6,2,4,6,4,8,12]
    # [1, 2, 2, 3, 4, 6]
    print(Solution().findOriginalArray(changed))
