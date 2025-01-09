"""
ans
  longest prefix suffix,
  LPS
  It stores, for each prefix of sub, the length of the longest proper prefix that is also a suffix.
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.frequency = 0
        self.child_nodes = {}


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        def insert(root, word):
            current_node = root
            for char in word:
                if char not in current_node.child_nodes:
                    current_node.child_nodes[char] = TrieNode()
                current_node = current_node.child_nodes[char]
                current_node.frequency += 1

        def is_substring(root, word):
            current_node = root
            for char in word:
                current_node = current_node.child_nodes[char]
            return current_node.frequency > 1

        root = TrieNode()

        for word in words:
            for start_index in range(len(word)):
                insert(root, word[start_index:])

        for word in words:
            if is_substring(root, word):
                ans.append(word)

        return ans

    def stringMatching1(self, words: List[str]) -> List[str]:
        ans = set()
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.add(words[i])

        return list(ans)