from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = [0] * 26
        for i, c in enumerate(s):
            last_occurrence[ord(c) - ord("a")] = i

        start = end = 0
        ans = []
        for i, c in enumerate(s):
            end = max(end, last_occurrence[ord(c) - ord("a")])

            if i == end:
                ans.append(i - start + 1)
                start = i + 1

        return ans