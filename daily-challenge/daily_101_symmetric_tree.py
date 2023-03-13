from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(node1, node2):

            # print(f'node1: {node1.val if node1 else None}, node2: {node2.val if node2 else None}')

            # Leaf
            if not node1 and not node2:
                return True
            # One end of subtree is missing so cannot recursion and not mirrow
            elif not node1 or not node2:
                return False

            else:
                return (
                    # Check node itself
                    node1.val == node2.val
                    # Check outward direction of a tree
                    and is_mirror(node1.left, node2.right)
                    # Check inward direction of a tree
                    and is_mirror(node1.right, node2.left)
                )

        return is_mirror(root, root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    """
        2
      3   3
     4 5   4
    """

    root = TreeNode(2)

    root.left = TreeNode(3)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print(Solution().isSymmetric(root))


