"""
Naive
  If current character has k - 1 adjacent same characters to the right, remove them
    curr pointer gets a character from given s and save the characters that aren't removed to a buffer
    One scan is finished, this buffer becomes the next s to iterate
  Before scanning removed flag initialized to be false
  After scan, if the flag is still false, no more to remove, so return
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#", 0]]

        for ch in s:

            if stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([ch, 1])

        return "".join(ch * count for ch, count in stack)

