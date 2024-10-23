# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        queue = collections.deque()
        queue.append(root)
        level_sums = []

        while queue:

            level_sum = 0

            for _ in range(len(queue)):

                curr = queue.popleft()
                level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            level_sums.append(level_sum)

        print(level_sums)

        # Second BFS
        queue.append(root)
        level_index = 1
        root.val = 0
        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                sibling_sum = (
                        (curr.left.val if curr.left else 0)
                        + (curr.right.val if curr.right else 0)
                )

                if curr.left:
                    curr.left.val = level_sums[level_index] - sibling_sum
                    queue.append(curr.left)
                if curr.right:
                    curr.right.val = level_sums[level_index] - sibling_sum
                    queue.append(curr.right)

            level_index += 1

        return root