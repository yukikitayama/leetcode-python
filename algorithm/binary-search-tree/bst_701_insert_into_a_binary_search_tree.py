from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left

            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right

        return TreeNode(val)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 5
    print(Solution().insertIntoBST(root, val))
