"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

https://leetcode.com/problems/binary-tree-vertical-order-traversal/description
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_vertical_traversals(self, root):
        if not root:
            return []

        col_to_vals = collections.defaultdict(list)

        # BFS
        queue = collections.deque()
        # [(node, col_index)]
        queue.append((root, 0))
        while queue:

            for _ in range(len(queue)):

                node, col = queue.popleft()
                col_to_vals[col].append(node.val)

                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))

        # {-1: [a, c], 0: [d, e], 1: [t, g]}
        # cols = list(col_to_vals.keys())
        # cols.sort()
        # ans = []
        # for col in cols:
        #     ans.append(col_to_vals[col])

        min_i = min(col_to_vals.keys())
        max_i = max(col_to_vals.keys())
        ans = []
        for i in range(min_i, max_i + 1):
            if i in col_to_vals:
                ans.append(col_to_vals[i])

        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
ans = Solution().get_vertical_traversals(root)
print(ans)
ans = Solution().get_vertical_traversals(None)
print(ans)
