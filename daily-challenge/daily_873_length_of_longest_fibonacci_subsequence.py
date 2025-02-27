"""
distinct integers
strictly increasing

if we know the first two numbers of our subsequence, we can calculate all possible next numbers in the sequence.

dp[i][j] represents the length of the longest Fibonacci-like sequence that ends with arr[i] and arr[j]
The indices i and j correspond to positions in our input array, with j always greater than i to maintain the strictly increasing order of the sequence.
If these are the last two numbers of our sequence, then the number that came before them must be arr[j] - arr[i]
If this difference exists in our array and occurs before arr[i], we can extend a previous sequence to include arr[j].
"""

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0

        dp = [[0] * len(arr) for _ in range(len(arr))]
        val_to_idx = {num: i for i, num in enumerate(arr)}

        for curr in range(len(arr)):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                if prev_idx >= 0 and diff < arr[prev]:
                    dp[prev][curr] = dp[prev_idx][prev] + 1
                else:
                    dp[prev][curr] = 2

                ans = max(ans, dp[prev][curr])

        # ans: 2 isn't fibonacci sequence, but it will appear in the process of DP
        return ans if ans > 2 else 0

    def lenLongestFibSubseq1(self, arr: List[int]) -> int:
        ans = 0

        num_set = set(arr)

        for start in range(len(arr)):
            for next_ in range(start + 1, len(arr)):

                prev = arr[next_]
                curr = arr[start] + arr[next_]
                curr_len = 2

                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    ans = max(ans, curr_len)

        return ans
