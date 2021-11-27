"""
- Use Trie and DFS
  - Trie because prefixes of strings are involved

"""


from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.word = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            node = node.children[c]

        node.isEnd = True
        node.word = word

    def bfs(self):
        q = collections.deque([self.root])

        res = ''

        while q:
            cur = q.popleft()
            # cur.children is object of defaultdict
            # so .values() gives us the values TrieNode objects
            for n in cur.children.values():
                # If isEnd is True, it means the current word exists in words
                if n.isEnd:
                    q.append(n)
                    # If it finds a longer word, or if the current word is lexicographically smaller
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word

        return res


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)

        # print(f'children: {trie.root.children}, isEnd: {trie.root.isEnd}, word: {trie.root.word}')
        # children = trie.root.children['w']
        # print(f'children: {children.children}, isEnd: {children.isEnd}, word: {children.word}')
        # children = children.children['o']
        # print(f'children: {children.children}, isEnd: {children.isEnd}, word: {children.word}')
        # children = children.children['r']
        # print(f'children: {children.children}, isEnd: {children.isEnd}, word: {children.word}')
        # children = children.children['l']
        # print(f'children: {children.children}, isEnd: {children.isEnd}, word: {children.word}')
        # children = children.children['d']
        # print(f'children: {children.children}, isEnd: {children.isEnd}, word: {children.word}')

        return trie.bfs()


"""
Complexity
- Time and space is O(sum of w_i), w_i is words[i]
"""


words = ["w","wo","wor","worl","world"]  # world
# words = ["a","banana","app","appl","ap","apply","apple"]  # apple
words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
# breakfast
print(Solution().longestWord(words))


