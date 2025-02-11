"""
stack
list compare
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_list = list(part)
        for ch in s:

            stack.append(ch)

            if len(stack) >= len(part_list):
                if stack[-len(part_list):] == part_list:
                    for _ in range(len(part_list)):
                        stack.pop()

        return "".join(stack)
