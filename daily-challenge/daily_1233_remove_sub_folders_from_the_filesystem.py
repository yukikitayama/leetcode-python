"""
prefix, trie
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.is_end_of_folder = False
        self.children = {}


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # Put all the paths to Trie
        for path in folder:

            curr = self.root

            path_split = path.split("/")

            for p in path_split:

                if p == "":
                    continue

                if p not in curr.children:
                    curr.children[p] = TrieNode()
                curr = curr.children[p]

            curr.is_end_of_folder = True

        # Check each path and collect non-subfolders
        ans = []

        for path in folder:

            curr = self.root

            path_split = path.split("/")
            is_subfolder = False

            for i, p in enumerate(path_split):

                if p == "":
                    continue

                next_ = curr.children[p]

                if next_.is_end_of_folder and i != len(path_split) - 1:
                    is_subfolder = True

                curr = next_

            if not is_subfolder:
                ans.append(path)

        return ans