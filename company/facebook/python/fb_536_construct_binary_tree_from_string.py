"""
- DFS
- Iterate string from left to right

- When encounter left-open parenthesis, call recursion
- When encountering right-close parenthesis, stop recursion
- Pair the current right-close parenthesis with the nearest left-open parenthesis
  to make the most recent subtree
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        return self.string_to_tree(s, 0)[0]

    def get_number(self, s: str, index: int) -> (int, int):
        """

        :param s: The given string
        :param index: The index to get a character from the given string
        :return:
        """
        # A number could be negative
        is_negative = False
        if s[index] == '-':
            is_negative = True
            index = index + 1

        # A number could be greater than 9
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1

        # The returned index is one step after the current number,
        # so it's the start index for the next character
        return number if not is_negative else -number, index

    def string_to_tree(self, s: str, index: int) -> (TreeNode, int):
        """

        :param s: The given string
        :param index: Index to get a character in the given string
        :return:
        """
        if index == len(s):
            return None, index

        value, index = self.get_number(s, index)
        node = TreeNode(value)

        if index < len(s) and s[index] == '(':
            node.left, index = self.string_to_tree(s, index + 1)

        # if node.left because the problem says always start to construct the left child first
        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self.string_to_tree(s, index + 1)

        # If see ')' stop recursion, otherwise no need to increment index because
        # it's the end of the given string; index == len(s)
        return node, index + 1 if index < len(s) and s[index] == ')' else index


if __name__ == '__main__':
    s = "4(2(3)(1))(6(5))"
    print(Solution().str2tree(s))
