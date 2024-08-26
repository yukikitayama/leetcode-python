"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        ans = []

        if not root:
            return ans

        def recursion(node):

            if not node.children:
                ans.append(node.val)
                return

            for next_ in node.children:
                recursion(next_)

            ans.append(node.val)

        recursion(root)

        return ans
