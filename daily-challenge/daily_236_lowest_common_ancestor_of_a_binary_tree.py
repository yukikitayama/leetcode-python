class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def recursion(node):

            nonlocal ans

            if not node:
                return False

            left = recursion(node.left)
            right = recursion(node.right)

            mid = False
            if node == p or node == q:
                mid = True

            if int(mid) + int(left) + int(right) >= 2:
                ans = node

            return mid or left or right

        recursion(root)
        return ans


if __name__ == '__main__':