from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def is_good(i, j, k):
            return (
                abs(arr[i] - arr[j]) <= a
                and abs(arr[j] - arr[k]) <= b
                and abs(arr[i] - arr[k]) <= c
            )

        ans = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if is_good(i, j, k):
                        ans += 1

        return ans