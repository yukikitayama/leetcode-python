"""
- BFS
"""


import collections
import pprint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        child_val_to_parent_node = {root.val: None}
        queue = collections.deque([root])

        while queue:

            node = queue.popleft()

            if node.left:
                child_val_to_parent_node[node.left.val] = node
                queue.append(node.left)
            if node.right:
                child_val_to_parent_node[node.right.val] = node
                queue.append(node.right)

        # for k, v in child_val_to_parent_node.items():
        #     print(f'child: {k}, parent: {v.val if v else "None"}')

        # Edge case: If either p or q does not exist, return None
        if p.val not in child_val_to_parent_node or q.val not in child_val_to_parent_node:
            return None

        # Find the lowest ancestor of p
        # The while loop stops when it reached the root, because parent of root is
        # initialized to be None
        # So ancestors set contains nodes up to root inclusively
        ancestors = set()
        while p:
            ancestors.add(p.val)
            # p is overwritten to be parent
            p = child_val_to_parent_node[p.val]

        # If q.val in ancestor, q is the lowest common ancestor,
        # because while going up from p to root, it passed q
        # If q.val not in ancestor, q is below p level, so
        # in this while loop q needs to pass the ancestor of p
        while q and q.val not in ancestors:
            q = child_val_to_parent_node[q.val]

        return q


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = TreeNode(5)
    q = TreeNode(1)
    # 3
    q = TreeNode(4)
    # 5
    print(Solution().lowestCommonAncestor(root, p, q).val)
