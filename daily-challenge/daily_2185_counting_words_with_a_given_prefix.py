from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        trie = TrieNode()

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
                curr.count += 1

        curr = trie
        for p in pref:
            if p in curr.children:
                curr = curr.children[p]
            else:
                return 0
        return curr.count

    def prefixCount1(self, words: List[str], pref: str) -> int:
        ans = 0

        for word in words:
            if word.startswith(pref):
                ans += 1

        return ans