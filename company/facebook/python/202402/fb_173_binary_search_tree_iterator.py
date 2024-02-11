"""
Naive
  At initialization
    inorder traversal,
    create a list of number in ascending order
    pointer index -1
    initial number float(-inf)
  hasNext
    check if pointer is less than the inorder list
  next
    increment pointer index
    return number at the pointer index
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.nums = []

    #     def inorder(node):
    #         if not node.left and not node.right:
    #             self.nums.append(node.val)
    #             return

    #         if node.left:
    #             inorder(node.left)
    #         self.nums.append(node.val)
    #         if node.right:
    #             inorder(node.right)

    #     inorder(root)

    #     self.pointer = -1

    # def next(self) -> int:
    #     self.pointer += 1
    #     return self.nums[self.pointer]

    # def hasNext(self) -> bool:
    #     return self.pointer < len(self.nums) - 1

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # At init needs to call otherwise hasNext will be error
        self.leftmost_inorder(root)

    def leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top_node = self.stack.pop()

        if top_node.right:
            self.leftmost_inorder(top_node.right)

        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()