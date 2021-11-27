from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last_index = {}
        for i, char in enumerate(s):
            char_to_last_index[char] = i

        curr_start = 0
        curr_max_end = 0

        ans = []

        for i, char in enumerate(s):

            curr_max_end = max(curr_max_end, char_to_last_index[char])

            if i == curr_max_end:
                ans.append(i - curr_start + 1)

                curr_start = i + 1

        return ans