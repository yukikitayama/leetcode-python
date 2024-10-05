from typing import List


class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:

            i = ord(c) - ord("a")

            if curr.next[i] is None:
                curr.next[i] = TrieNode()

            curr.next[i].cnt += 1

            curr = curr.next[i]

    def count(self, word):

        curr = self.root

        res = 0

        for c in word:
            i = ord(c) - ord("a")

            res += curr.next[i].cnt
            curr = curr.next[i]

        return res

    def sumPrefixScores(self, words: List[str]) -> List[int]:

        N = len(words)

        for i in range(N):
            self.insert(words[i])

        ans = [0] * N

        for i in range(N):
            ans[i] = self.count(words[i])

        return ans
