"""
String order is preorder, so let's do DFS in preorder

dfs(i)
  i is index for given string

  create current number with while loop until current string isn't number

  create a node with current number

  if next string is "("
    get left child
    set left child to current node left

  if next string is ")", return

  if next string is "("
  get right child
  set right child to current node right

  return node

Answer
  Tree is between a pair of matching brackets
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

        def get_number(i):
            is_negative = False

            if s[i] == "-":
                is_negative = True
                i += 1

            # Create a val for a node
            curr_num = 0
            # Number can be more than 9
            while i < len(s) and s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
                i += 1

            # Here i points at string after the current number
            if is_negative:
                return -curr_num, i
            else:
                return curr_num, i

        def dfs(i):

            # Terminal
            if i == len(s):
                return None, i

            curr_num, next_index = get_number(i)
            curr_node = TreeNode(val=curr_num)

            # Left child
            if next_index < len(s) and s[next_index] == "(":
                left_child, next_index = dfs(next_index + 1)
                curr_node.left = left_child

            # Right child
            # if node.left comes from 'You always start to construct the left child node of the parent first if it exists'
            if curr_node.left and next_index < len(s) and s[next_index] == "(":
                right_child, next_index = dfs(next_index + 1)
                curr_node.right = right_child

            if next_index < len(s) and s[next_index] == ")":
                return curr_node, next_index + 1
            # ?
            else:
                return curr_node, next_index

            # s = "4(2(3)(1))(6(5))"

        root, index = dfs(0)

        return root
