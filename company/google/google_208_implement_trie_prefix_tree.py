from collections import defaultdict


class TrieNode:
    def __init__(self):
        # Key: a letter, value: TrieNode
        self.nodes = defaultdict(TrieNode)
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # curr is an object of TrieNode
        curr = self.root
        for char in word:
            # curr.nodes is an object of defaultdict(TrieNode)
            # add a new key and value is initialized with empty dictionary
            # this new TrieNode becomes an object called curr,
            # so curr goes 1 level down
            curr = curr.nodes[char]
        curr.isword = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # curr.nodes is dictionary
            if char not in curr.nodes:
                return False
            # Go 1 level down
            curr = curr.nodes[char]
        # If you can go to the bottom, it has a TrieNode with an empty dictionary ans isword: True
        return curr.isword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        # If above iteration did not hit False, successfull went through the path so return True
        return True


trie = Trie()
print(f'Root: node: {trie.root.nodes}, isword: {trie.root.isword}')
trie.insert('test')
trie.insert('yuki')
print(f'Root: node: {trie.root.nodes}, isword: {trie.root.isword}')
print(f'Level 1: node: {trie.root.nodes["t"].nodes}, isword: {trie.root.nodes["t"].isword}')
print(f'Level 2: node: {trie.root.nodes["t"].nodes["e"].nodes}, isword: {trie.root.nodes["t"].nodes["e"].isword}')
print(f'Level 3: node: {trie.root.nodes["t"].nodes["e"].nodes["s"].nodes}, isword: {trie.root.nodes["t"].nodes["e"].nodes["s"].isword}')
print(f'Level 4: node: {trie.root.nodes["t"].nodes["e"].nodes["s"].nodes["t"].nodes}, isword: {trie.root.nodes["t"].nodes["e"].nodes["s"].nodes["t"].isword}')
