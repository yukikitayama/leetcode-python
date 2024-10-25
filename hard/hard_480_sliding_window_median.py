from typing import List
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        ans = []
        window = []

        for i in range(len(nums)):

            # Once full, start popping
            # e.g. k: 3, i: 3 is 4th element, so pop
            if i >= k:
                window.remove(nums[i - k])

            # Maintain sorted order and insert
            bisect.insort(window, nums[i])

            if i >= (k - 1):

                # Odd
                if k % 2 != 0:
                    med = window[k // 2]

                # Even
                else:
                    med = (window[k // 2 - 1] + window[k // 2]) / 2

                ans.append(med)

        return ans