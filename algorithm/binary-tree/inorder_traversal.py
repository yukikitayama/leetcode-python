from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive approach
class RecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# Iterative approach
class IterativeSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans.append(curr.val)
            # When curr is a leaf, curr.right is None,
            # so the above while curr will be skipped
            curr = curr.right

        return ans
