"""
- recursively check whether root.left value is equal to root.right value
  - If not return False
  - If True, recursion
- Stop recursion when it reaches None, leaf
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_symmetric(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            return (node1.val == node2.val
                    and is_symmetric(node1.right, node2.left)
                    and is_symmetric(node1.left, node2.right))

        return is_symmetric(root, root)


"""
Time: O(n) by n being the number of nodes
Space: O(n)
"""