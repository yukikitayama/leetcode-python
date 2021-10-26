"""
- Iterative
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            queue = collections.deque([root])

            while queue:
                curr_node = queue.popleft()
                curr_node.left, curr_node.right = curr_node.right, curr_node.left

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return root


"""

"""


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
ans = Solution().invertTree(root)
print(ans.val)
print(ans.left.val)
print(ans.right.val)
print('None' if not ans.left.left else ans.left.left.val)
print(ans.left.right.val)
print(ans.right.left.val)
print(ans.right.right.val)





