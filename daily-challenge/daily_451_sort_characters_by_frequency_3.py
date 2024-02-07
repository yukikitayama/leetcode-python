"""
Counter
sorted, key, lambda
T: O(NlogN)
"""

import collections


class Solution:
    # def frequencySort(self, s: str) -> str:

    #     counter = collections.Counter(s)
    #     ans = [ch for ch in s]
    #     ans = sorted(ans, key=lambda ch: (-counter[ch], ch))

    #     return "".join(ans)

    def frequencySort(self, s: str) -> str:

        # Count frequency
        counter = collections.Counter(s)

        # Create bucket by max value
        # Index is freq, element is list of charachters of freq
        max_freq = max(counter.values())
        bucket = [[] for _ in range(max_freq + 1)]
        for k, v in counter.items():
            bucket[v].append(k)

        # From right of array, iterate and create ans
        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for ch in bucket[i]:
                ans.append(ch * i)
        return "".join(ans)
