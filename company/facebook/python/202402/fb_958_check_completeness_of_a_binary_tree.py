"""
I want None to happen after the rightmost last node in leaves

BFS
  When appending a node to queue,
    If a child doesn't exist, append None to queue
    If a child exists and append it to queue, check the last part of the queue
      If none is there, it's not complete

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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = collections.deque()
        queue.append(root)
        none_happened = False

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                print(curr)

                if curr is None:
                    none_happened = True
                else:
                    # What we care is only the appearance of node after None
                    # None after none is okay
                    if none_happened:
                        return False

                    # At the leaves, this appends manny None to queue
                    # but it's okay. It won't affect above conditions
                    queue.append(curr.left)
                    queue.append(curr.right)

        return True




