from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional) -> List[int]:

        ans = []
        stack = [root]

        while stack:

            # Popped by right -> left
            curr = stack.pop()

            if curr:

                # Appended by root -> right -> left
                # Appending order is reverse of postorder traversal
                ans.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)

        # Finally order the list to left -> right -> root for postorder traversal
        ans.reverse()

        return ans
