"""
- level order traversal
- If last in a level, append to answer
"""


from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        if not root:
            return ans

        # If pick right child always, right side view
        def dfs(node, level):
            if level == len(ans):
                ans.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1)

        dfs(root, 0)
        return ans


class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = collections.deque()

        if root:
            queue.append(root)

        ans = []

        while queue:

            curr_length = len(queue)

            for i in range(curr_length):

                curr_node = queue.popleft()

                if i == curr_length - 1:
                    ans.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    # [1, 3, 4]
    print(Solution().rightSideView(root))
