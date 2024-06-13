from typing import List
import collections


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        def counting_sort(arr):
            counter = collections.Counter(arr)
            min_ = min(arr)
            max_ = max(arr)
            res = []
            for curr in range(min_, max_ + 1):
                while curr in counter:
                    res.append(curr)
                    counter[curr] -= 1
                    if counter[curr] == 0:
                        del counter[curr]
            return res

        expected = counting_sort(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans

    def heightChecker1(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans