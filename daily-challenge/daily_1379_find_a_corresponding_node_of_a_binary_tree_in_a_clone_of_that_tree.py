"""
- If all the values are unique, compare val
- If repeated values are allowed, compare reference to the node
"""


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_original = collections.deque([original])
        queue_cloned = collections.deque([cloned])

        while queue_original:

            curr_original = queue_original.popleft()
            curr_cloned = queue_cloned.popleft()

            if curr_original is target:
                return curr_cloned

            if curr_original.left:
                queue_original.append(curr_original.left)
                queue_cloned.append(curr_cloned.left)

            if curr_original.right:
                queue_original.append(curr_original.right)
                queue_cloned.append(curr_cloned.right)


class Solution1:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        ans = None

        def inorder(original_curr, cloned_curr):

            nonlocal ans

            if original_curr:
                inorder(original_curr.left, cloned_curr.left)
                if original_curr is target:
                    ans = cloned_curr
                inorder(original_curr.right, cloned_curr.right)

        inorder(original, cloned)

        return ans


