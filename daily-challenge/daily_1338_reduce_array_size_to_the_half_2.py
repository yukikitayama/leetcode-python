from typing import List
import collections


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counter = collections.Counter(arr)

        counts = [v for k, v in counter.most_common()]

        n = len(arr)
        curr = n
        ans = 0

        for c in counts:
            ans += 1
            curr -= c

            if curr <= n // 2:
                return ans


if __name__ == '__main__':
    arr = [3,3,3,3,5,5,5,2,2,7]
    arr = [7, 7, 7, 7, 7, 7]
    print(Solution().minSetSize(arr))