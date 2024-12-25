from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def compute_num_swaps(values):
            res = 0
            sorted_copy = sorted(values)
            val_to_idx = {v: i for i, v in enumerate(values)}
            for i in range(len(values)):
                if values[i] != sorted_copy[i]:
                    res += 1
                    # Swap
                    correct_idx = val_to_idx[sorted_copy[i]]
                    val_to_idx[values[i]] = correct_idx
                    values[correct_idx] = values[i]
            return res

        queue = collections.deque()
        queue.append(root)
        ans = 0
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += compute_num_swaps(values)

        return ans