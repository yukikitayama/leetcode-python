"""
- Easy approach is, in constructor make a list of inorder traversal of BST
  - Keep index
  - Space O(N)
  - Time, constructor O(N), other methods O(1)

"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.last = root
        # Stack bottom is parent node, stack top is leaf child left node
        self.stack = []
        self.arr = []
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.stack or self.last or self.pointer < len(self.arr) - 1

    def next(self) -> int:
        self.pointer += 1

        if self.pointer == len(self.arr):
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            curr = self.stack.pop()
            self.last = curr.right
            self.arr.append(curr.val)

        return self.arr[self.pointer]

    def hasPrev(self) -> int:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]


class BSTIterator1:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = self._inorder(root)
        self.n = len(self.arr)
        self.pointer = -1

    def hasNext(self) -> bool:
        # -1 because if pointer is n - 1, pointer is at the end of the array
        # so there's no next
        return self.pointer < self.n - 1

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]

    def hasPrev(self) -> int:
        # When pointer is 0, arr[pointer] exists, but the prev doesn't exist
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]

    def _inorder(self, node):
        return self._inorder(node.left) + [node.val] + self._inorder(node.right) if node else []


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    obj = BSTIterator(root)
    print(obj.arr)
    print(obj.next())
    print(obj.next())
    print(obj.prev())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.hasPrev())
    print(obj.prev())
    print(obj.prev())
