from typing import List
import collections


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.content = ''


class FileSystem:
    def __init__(self):
        self.root = Node()

    def find(self, path):
        curr = self.root
        if len(path) == 1:
            return self.root
        # [1:] because [0] is ''
        for word in path.split('/')[1:]:
            curr = curr.child[word]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path)
        # If file
        if curr.content:
            return [path.split('/')[-1]]
        # If directory
        # child is a hashmap
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        # First make a node object
        curr = self.find(filePath)
        # Add content to content attribute
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        # First get a node
        curr = self.find(filePath)
        return curr.content
