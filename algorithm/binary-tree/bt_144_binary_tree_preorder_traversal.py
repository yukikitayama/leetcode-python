from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Morris traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        output = []

        while node:

            if not node.left:
                output.append(node.val)
                node = node.right

            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left

                else:
                    predecessor.right = None
                    node = node.right

        return output


class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                ans.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().preorderTraversal(root))
