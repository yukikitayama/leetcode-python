"""
iterate s by index
  when index is not the index in space
    append current character to answer list of characters
  when index is equal to index in spaces
    append space to answer list, then insert current character
    increment index to spaces array
"""

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = []
        space_pointer = 0

        for i in range(len(s)):

            if space_pointer < len(spaces) and i == spaces[space_pointer]:
                ans.append(" ")
                space_pointer += 1

            ans.append(s[i])

        return "".join(ans)
