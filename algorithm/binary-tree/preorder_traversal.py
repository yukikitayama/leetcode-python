from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        # Preorder traversal is DFS using stack
        stack = [root]

        while stack:

            # By popping the top of the stack, left is processed before right
            curr = stack.pop()

            if curr:

                # Need to push current value first because preorder is root -> left -> right
                ans.append(curr.val)

                # Push right before left to the stack,
                # so right will be delayed to be processed
                if curr.right:
                    stack.append(curr.right)

                # Push at the last, but popped first because of stack
                if curr.left:
                    stack.append(curr.left)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().preorderTraversal(root))
