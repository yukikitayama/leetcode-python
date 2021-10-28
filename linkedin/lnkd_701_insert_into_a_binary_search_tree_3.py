"""
- refactered iteration
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        # When root is None, it skips while loop and go to the end return statement,
        # which just makes TreeNode object with the given val
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root

        return TreeNode(val)



"""
- Let h be the height of tree, and time is O(h)
  - That is, O(log n) because in every level, it reduces the number of nodes to search by half
"""


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
val = 5
# root = []
# val = 5
ans = Solution().insertIntoBST(root, val)
print(ans.val)
print(ans.left.val, ans.right.val)
print(ans.left.left.val, ans.left.right.val, ans.right.left.val, None)


