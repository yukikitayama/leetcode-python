from typing import List
import collections


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        # Append the current character from the left
        # Older characters at the right of the queue
        # Newer characters at the left of the queue
        # e.g. stream: 'a', 'b', 'c', self.stream: ['c', 'b', 'a']
        self.stream = collections.deque([])

        # Make Trie from a list of words
        for word in set(words):
            node = self.trie
            # Reversed word
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            # Mark the end of word
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        # Get a character from the left of the queue,
        # meaning getting a newer character first
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]

        return '$' in node


"""
Complexity
- Let N be the length of words, and M be the average word length
- Time
  - Constructor is O(MN) for each word, it takes M to examine or create a node in the trie
  - query is O(M) for a max word length, i.e. the depth of trie
  
words: ['cd']
trie:
root
  - d
    - c
stream: ['c'], self.stream: ['c'], query: F
stream: ['d'], self.stream: ['d', 'c'], query: T
"""
