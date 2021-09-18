from typing import List, Optional
from collections import defaultdict
import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def tuplify(root):
            if root:
                tuple = root.val, tuplify(root.left), tuplify(root.right)
                trees[tuple].append(root)
                return tuple

        # Key: tuple of (node.val, left subtree, right subtree),
        # Value: a list of TreeNodes which have the same structure.
        # Equal subtrees have the same key and get collected in the same list
        trees = defaultdict(list)
        tuplify(root)

        # pprint.pprint(trees)
        # print()

        # trees.values() gives us lists
        # If there are multiple same subtrees, roots length is bigger than 1
        # in that case, you have something when roots[1:], so if is True,
        # meaning we have same subtrees, so return one of them
        # If the subtree is unique, list length is 1, so roots[1:] gives us empty list [] (no out of bound error)
        # and if [] is False, so does not return
        return [roots[0] for roots in trees.values() if roots[1:]]


"""
Time complexity
Let n be the number of nodes in the tree. O(n**2)

Space complexity
O(n)
"""


root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))
print(Solution().findDuplicateSubtrees(root))

