from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = word

    def get_root(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return word
            curr = curr.children[c]
            if curr.end_of_word:
                return curr.end_of_word
        # e.g. trie: a -> b, word: a
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build trie
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)

        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.get_root(words[i])

        return " ".join(words)

    def replaceWords1(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dictionary_set = set(dictionary)

        def find_shortest_root(word):
            for i in range(len(word)):
                curr = word[0:i]
                if curr in dictionary_set:
                    return curr
            return word

        for i in range(len(words)):
            words[i] = find_shortest_root(words[i])

        return " ".join(words)
