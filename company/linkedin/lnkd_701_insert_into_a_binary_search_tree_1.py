"""
- If current node val > val, val goes to left
- If current node val < val, val goes to right
- Continue as long as current node is not None
- If current node is None, val is inserted to the current position

-
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr_node = root

        is_left = True

        while curr_node:

            prev_node = curr_node

            if curr_node.val > val:
                curr_node = curr_node.left
                is_left = True
            elif curr_node.val < val:
                curr_node = curr_node.right
                is_left = False

        if is_left:
            prev_node.left = TreeNode(val)
        else:
            prev_node.right = TreeNode(val)

        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
val = 5
root = []
val = 5
ans = Solution().insertIntoBST(root, val)
print(ans.val)
print(ans.left.val, ans.right.val)
print(ans.left.left.val, ans.left.right.val, ans.right.left.val, None)


