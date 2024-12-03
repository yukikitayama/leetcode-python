from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []

        i_s = 0
        for i in range(len(s)):

            if i_s < len(spaces) and i == spaces[i_s]:
                ans.append(" ")
                i_s += 1

            ans.append(s[i])

        return "".join(ans)