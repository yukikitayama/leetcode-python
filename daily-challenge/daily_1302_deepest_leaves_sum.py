"""
- bfs
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        next_level = collections.deque([root])

        while next_level:

            curr_level = next_level
            next_level = collections.deque()

            for node in curr_level:

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return sum([node.val for node in curr_level])


class Solution2:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        depth = 0
        queue = collections.deque([(root, 0)])

        while queue:

            curr_node, curr_depth = queue.popleft()

            if not curr_node.left and not curr_node.right:

                if curr_depth > depth:
                    depth = curr_depth
                    ans = curr_node.val

                elif curr_depth == depth:
                    ans += curr_node.val

            else:
                if curr_node.left:
                    queue.append((curr_node.left, curr_depth + 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_depth + 1))

        return ans


class Solution1:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        depth = 0
        # Stack: [(node, depth), ...]
        stack = [(root, 0)]

        while stack:

            node, curr_depth = stack.pop()

            # If leaf, try computing answer, but might be overwritten
            if not node.left and not node.right:

                if curr_depth > depth:
                    ans = node.val
                    depth = curr_depth

                elif curr_depth == depth:
                    ans += node.val

            # It hasn't reached the deepest so keep iterating
            else:
                # First append right, because of LIFO to use left first later
                if node.right:
                    stack.append((node.right, curr_depth + 1))
                if node.left:
                    stack.append((node.left, curr_depth + 1))

        return ans


if __name__ == '__main__':
    pass
