"""
- If current val is between p value and q value
  - current node is the lowest common ancestor
- If current val is bigger than both p and q
  - Move current node to left
- If current val is smaller than p and q
  - Move to right
- If current val is equal to either p or q
  - current node is the lowest common ancestor
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # print(f'root.val: {root.val}, p.val: {p.val}, q.val: {q.val}')

        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        if p.val < root.val and q.val < root.val:
            ans = self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            ans = self.lowestCommonAncestor(root.right, p, q)

        return ans


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = TreeNode(2)
# q = TreeNode(4)
q = TreeNode(8)
ans = Solution().lowestCommonAncestor(root, p, q)
print(ans.val)










