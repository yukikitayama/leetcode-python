from typing import Optional, List
import collections
import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def get_id(root):
            if root:
                id = tree_id[root.val, get_id(root.left), get_id(root.right)]
                trees[id].append(root)
                return id

        trees = collections.defaultdict(list)
        tree_id = collections.defaultdict()
        tree_id.default_factory = tree_id.__len__
        get_id(root)

        pprint.pprint(trees)
        pprint.pprint(tree_id)

        ans = []
        for value in trees.values():
            if len(value) > 1:
                ans.append(value[0])

        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
print(Solution().findDuplicateSubtrees(root))
