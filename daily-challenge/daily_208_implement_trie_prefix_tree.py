"""
Complexity
- Let m be the length of a word
- insert
  - Time is O(m) to iterate each character in a word
  - Space is O(m) to make m linked TrieNode objects
- search
  - Time is O(m) to iterate each character in a word
  - Space is O(1) because it does not create new objects, only iterating the existing objects
- startsWith
  - Time is O(m) to iterate each character in a word
  - Space is O(1) because it does not create new objects
"""


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # nodes is defaultdict
            # The key is a character and the value is TrieNode object by default
            # The next curr is automatically TrieNode
            # So the next curr also has nodes attribute and it's defaultdict
            curr = curr.nodes[char]
        curr.isword = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        # When all the characters in word are exhausted,
        # if previously inserted the current word, isword was set to True by insert()
        # But if not, and the current word is just a prefix of previously inserted word
        # isword was left to be False
        return curr.isword

    def startsWith(self,prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]

        # When it reached here, it means all the characters in prefix are exhausted
        # it means the prefix exists by some of words previously inserted
        return True


obj = Trie()
obj.insert('abc')
print(obj.search('abc'))
print(obj.search('ab'))

