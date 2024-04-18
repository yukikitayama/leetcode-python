"""
queue [(node, array of characters)]
ans
if leaf,
  updated ans with min
  found_leaf true

chr(ord("a") + val)
"""

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        queue = collections.deque()
        queue.append((root, []))

        while queue:

            for _ in range(len(queue)):

                node, comb = queue.popleft()

                # Leaf
                if not node.left and not node.right:
                    comb.append(node.val)
                    string = [chr(ord("a") + num) for num in comb]
                    string.reverse()
                    string = "".join(string)
                    if not ans:
                        ans = string
                    else:
                        ans = min(ans, string)

                if node.left:
                    queue.append((node.left, comb[:] + [node.val]))
                if node.right:
                    queue.append((node.right, comb[:] + [node.val]))

            print(queue)

        return ans