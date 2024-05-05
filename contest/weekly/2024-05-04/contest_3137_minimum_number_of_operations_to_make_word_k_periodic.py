"""
Greedy

Find candidates
  iterate left to right - k
    length of k
  Substring with the largest count is the string for k-periodic
Compute remain = length - the count * k
Return remain // k
"""

import collections


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:

        counter = collections.Counter()
        s = None
        max_so_far = 0

        for left in range(0, len(word) - k + 1, k):

            right = left + k

            substring = word[left:right]

            counter[substring] += 1

            if counter[substring] > max_so_far:
                s = substring
                max_so_far = counter[substring]

        # print(counter)
        # print(s)
        # print(max_so_far)

        remain = len(word) - counter[s] * k

        return remain // k