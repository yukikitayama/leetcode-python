from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        answer = []
        level = 0
        queue = [root]

        while queue:

            answer.append([])

            for i in range(len(queue)):

                node = queue.pop(0)

                answer[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return answer


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# root = TreeNode(1)
root = None

sol = Solution()
answer = sol.levelOrder(root)
print(f'Answer: {answer}')
