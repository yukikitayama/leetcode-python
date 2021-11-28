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
        self.index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.recursive_build(0, len(preorder) - 1, self.index, preorder, inorder)

    def recursive_build(self, left: int, right: int, index, preorder, inorder) -> TreeNode:
        if left > right:
            # print('Return None')
            return None

        print(f'self.index of preorder[self.index]: {self.index}')
        root_value = preorder[self.index]

        root = TreeNode(root_value)

        self.index += 1

        print(f'root_value: {root_value}, self.index: {self.index}, '
              f'left: {left}, inorder.index(root_value) - 1: {inorder.index(root_value) - 1}')
        root.left = self.recursive_build(left, inorder.index(root_value) - 1, self.index, preorder, inorder)
        print(f'root_value: {root_value}, self.index: {self.index}, '
              f'inorder.index(root_value) + 1: {inorder.index(root_value) + 1}, right: {right})')
        root.right = self.recursive_build(inorder.index(root_value) + 1, right, self.index, preorder, inorder)

        return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().buildTree(preorder, inorder)
print(root)
print(root.left, root.right)
print(root.left.left, root.left.right, root.right.left, root.right.right)