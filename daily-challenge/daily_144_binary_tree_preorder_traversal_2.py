from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        curr = root

        while curr:

            if not curr.left:
                ans.append(curr.val)
                # curr.right uses a pointer to go back
                curr = curr.right

            else:
                last = curr.left

                while last.right and last.right != curr:
                    last = last.right

                if not last.right:
                    ans.append(curr.val)
                    # Make a pointer to go back
                    last.right = curr
                    # Traverse current pointer
                    curr = curr.left

                else:
                    last.right = None
                    curr = curr.right

        return ans


