from typing import List, Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        ans = []

        queue = collections.deque()
        queue.append(root)

        while queue:

            curr_sum = 0
            curr_count = 0

            for _ in range(len(queue)):

                curr_node = queue.popleft()

                curr_sum += curr_node.val
                curr_count += 1

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            ans.append(curr_sum / curr_count)

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().averageOfLevels(root))
