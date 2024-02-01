"""
- BFS
- Hashmap where key is level and value is sum
- Update answer max sum after each level
"""


from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])

        curr_level = 1
        ans_max_level_so_far = 1

        max_sum_so_far = float('-inf')
        curr_sum = 0

        while queue:

            for _ in range(len(queue)):

                curr_node = queue.popleft()
                curr_sum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            if curr_sum > max_sum_so_far:
                ans_max_level_so_far = curr_level
                max_sum_so_far = curr_sum

            curr_level += 1
            curr_sum = 0

        return ans_max_level_so_far


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    print(Solution().maxLevelSum(root))
