import collections


class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            curr = curr.nodes[char]

        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]

        return curr.is_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]

        # When it reaches here, all the characters in prefix are exhausted
        # so prefix exists in some words previously inserted
        return True
