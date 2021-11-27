"""
- Iterative using parent pointers
  - First common node during the traversal is LCA node
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        # Hashmap with key child node and value parent node
        parent = {root: None}
        while p not in parent or q not in parent:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)

        # Get all the parents of p up to the root
        ancestors = set()
        while p:
            ancestors.add(p)
            # Get parent of current p
            p = parent[p]

        # Find the first ancestor common between p and q
        while q not in ancestors:
            q = parent[q]
        return q


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
ans = Solution().lowestCommonAncestor(root, root.left, root.right)
print(ans.val)
