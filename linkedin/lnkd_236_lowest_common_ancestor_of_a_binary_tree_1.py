class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def recurse_tree(node):

            # print(f'  node.val: {node.val}')

            nonlocal ans

            if not node:
                return False

            left = recurse_tree(node.left)
            right = recurse_tree(node.right)
            if node.val == p.val or node.val == q.val:
                mid = True
            else:
                mid = False

            # print(f'  mid: {mid}, left: {left}, right: {right}')

            if mid + left + right >= 2:
                # print('here')
                ans = node

            return mid or left or right

        recurse_tree(root)
        return ans


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
ans = Solution().lowestCommonAncestor(root, root.left, root.right)
print(ans.val)
