"""
simulation
  str2[:len(str1)]
  str2[-len(str1):]
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.poss_ends = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for i in range(len(word)):
            pr = word[i]
            su = word[len(word) - 1 - i]
            if (pr, su) not in cur.children:
                cur.children[(pr, su)] = TrieNode()
            cur = cur.children[(pr, su)]
            cur.poss_ends += 1

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            pr = word[i]
            su = word[len(word) - 1 - i]
            if (pr, su) not in cur.children:
                return 0
            cur = cur.children[(pr, su)]
        return cur.poss_ends


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        trie = Trie()

        # reversed [::-1] for i < j
        for word in words[::-1]:
            ans += trie.search(word)
            trie.insert(word)

        return ans

    def countPrefixSuffixPairs1(self, words: List[str]) -> int:

        ans = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                str1 = words[i]
                str2 = words[j]
                if str2[:len(str1)] == str1 and str2[-len(str1):] == str1:
                    ans += 1

        return ans