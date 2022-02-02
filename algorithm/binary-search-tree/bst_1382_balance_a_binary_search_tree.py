"""
- Given root of BST, do inorder traversal to get an array in an ascending order
- From the array, reconstruct BST to distribute equal number of left and right child to each left and right subtree
  - By separating the array from mid point
  - Eventually it will become height balanced
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder_traversal(node):
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []

        inorder = inorder_traversal(root)

        print(f'inorder: {inorder}')

        def bst(inorder_nodes):
            if not inorder_nodes:
                return None

            mid = len(inorder_nodes) // 2
            node = TreeNode(inorder_nodes[mid])
            node.left = bst(inorder_nodes[:mid])
            node.right = bst(inorder_nodes[mid + 1:])
            return node

        return bst(inorder)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    # root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)

    ans = Solution().balanceBST(root)
    print(ans.val)
    print(ans.left.val, ans.right.val)
    print(ans.left.left.val, ans.left.right, ans.right.left, ans.right.right)
