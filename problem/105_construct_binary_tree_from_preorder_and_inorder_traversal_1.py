from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'


class Solution:
    def __init__(self):
        self.preorder = None
        self.inorder_index_map = None
        self.preorder_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder

        self.inorder_index_map = {}
        for i, value in enumerate(inorder):
            self.inorder_index_map[value] = i

        return self.array_to_tree(0, len(preorder) - 1)

    def array_to_tree(self, left: int, right: int) -> TreeNode:
        if left > right:
            return None

        root_value = self.preorder[self.preorder_index]

        root = TreeNode(root_value)

        self.preorder_index += 1
        print(f'root_value: {root_value}, self.preorder_index: {self.preorder_index}, '
              f' self.inorder_index_map[root_value] - 1: {self.inorder_index_map[root_value] - 1}')

        root.left = self.array_to_tree(left, self.inorder_index_map[root_value] - 1)
        root.right = self.array_to_tree(self.inorder_index_map[root_value] + 1, right)

        return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
root = sol.buildTree(preorder, inorder)
print()
print(root)
print(root.left, root.right)
print(root.left.left, root.left.right, root.right.left, root.right.right)
