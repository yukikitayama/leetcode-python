from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        # deque left has nodes which has both left and right are empty, or only right is empty
        # deque right has bottom-rightmost node in the complete binary tree
        self.deque = collections.deque()
        self.root = root

        # q is a queue only used for initialization to fill self.deque
        q = collections.deque([root])
        while q:
            node = q.popleft()
            # If current node has both left and right child, it won't be in self.deque
            # So self.deque only contains leaves or only left has a child
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.deque[0]

        self.deque.append(TreeNode(val))

        # If left child is None, set insert a new node there
        # It means currently the tree is complete
        if not node.left:
            node.left = self.deque[-1]

        # If here, the bottom left in the tree has a few nodes at the leftmost
        # so insert a new node to the bottom level
        else:
            node.right = self.deque[-1]
            # Here, deque left side node has left and right child,
            # so no longer needed to connect child
            self.deque.popleft()

        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2))
    obj = CBTInserter(root)
