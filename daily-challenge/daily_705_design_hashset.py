from typing import Optional


class MyHashSet:
    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    def _hash(self, key) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Bucket:
    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return self.tree.searchBST(self.tree.root, value) is not None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def searchBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        if root is None or val == root.val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        elif val == root.val:
            return root

        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val


class MyHashSet1:
    def __init__(self):
        self.hash_key = 1999
        self.hash_set = [[] for _ in range(self.hash_key)]

    def add(self, key: int) -> None:
        hashed_index = key % self.hash_key
        if not self.hash_set[hashed_index]:
            self.hash_set[hashed_index].append(key)
        else:
            for value in self.hash_set[hashed_index]:
                if value == key:
                    return
            self.hash_set[hashed_index].append(key)

    def contains(self, key: int) -> bool:
        hashed_index = key % self.hash_key
        for value in self.hash_set[hashed_index]:
            if value == key:
                return True
        return False

    def remove(self, key: int) -> None:
        hashed_index = key % self.hash_key
        for i, value in enumerate(self.hash_set[hashed_index]):
            if value == key:
                self.hash_set[hashed_index].pop(i)
