from typing import List
import collections


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        # content remains '' if a path is just a directory path
        self.content = ''


class FileSystem:
    def __init__(self):
        self.root = Node()

    def find(self, path):
        # '/'
        if len(path) == 1:
            return self.root

        curr = self.root
        # Recursively update curr to the next Node
        # [1:] because the first element is empty '' after split('/')
        # e.g. '/a/b/c'.split('/'): ['', 'a', 'b', 'c']
        for word in path.split('/')[1:]:
            # child is an object of defaultdict with default Node object
            # So this not only traverses, but also make a Node object in mkdir() if word does not exist
            curr = curr.child[word]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path)

        # If curr.content is not '', the path is not directory path, but a file path
        # so path.split('/')[-1] gets only the part of file name
        # e.g. /a/b/c.split('/'): ['', 'a', 'b', 'c'], that [-1]: 'c', so ['c']
        if curr.content:
            return [path.split('/')[-1]]

        # Path is a directory path, so return a list of file and directory name
        # in this directory in lexicographic order
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content


fs = FileSystem()
path = '/'
print(path.split('/'))
path = '/a/b/c'
print(path.split('/'))
print(path.split('/')[-1])
