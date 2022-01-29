"""
- Two implementations
  1. Flatten BST to inorder array, and use index to iterate the array for next
    - Pros
      - Easy to implement
    - Cons
      - Constructor time takes O(N)
      - Space takes O(N) for the inorder array
  2. Use stack to simulate inorder traversal
    - Pros
      - In the amortized time, next() takes time O(1)
      - Space takes O(H) where H is the tree height for the stack
        - Stack appending continues until it sees a leaf in tree, so O(H), not O(N)
    - Cons
      - Need to spend time implementing constructor and next()
      - In the worst case of skewed tree, next() takes time O(N)
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self._leftmost_inorder(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    obj = BSTIterator(root)
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
