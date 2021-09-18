from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        counter = Counter(nums)

        # print(f'counter: {counter}')

        for num in sorted(counter):

            if counter[num] > 0:

                for i in range(k)[::-1]:

                    # Use now, so decrement it
                    # Bigger number needs to have the same amount as the current num
                    # to make multiple consecutive sequences.
                    # So -= counter[num], not -= 1
                    counter[num + i] -= counter[num]

                    if counter[num + i] < 0:
                        return False

        return True


nums = [1,2,3,3,4,4,5,6]
k = 4
nums = [3,3,2,2,1,1]
k = 3
# nums = [1,2,3,4]
# k = 3
print(Solution().isPossibleDivide(nums, k))
