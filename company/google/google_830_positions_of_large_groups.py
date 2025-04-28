from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        left = right = 0
        while right < len(s):

            while right < len(s) - 1 and s[right] == s[right + 1]:
                right += 1

            if right - left + 1 >= 3:
                ans.append([left, right])

            right += 1
            left = right

        return ans