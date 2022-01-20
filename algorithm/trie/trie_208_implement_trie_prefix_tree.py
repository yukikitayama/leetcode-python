import collections


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            # A new Node object is made on the fly
            # curr.child[c] returns a new Node object or existing Node object
            curr = curr.child[c]

        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        # This could return False, if search word exhaust in the middle
        # e.g. Trie contains "book", and search(boo) stops in the middle
        # b -> bo -> boo path exists in Trie, but boo doesn't exist as a word yet.
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        return True


if __name__ == '__main__':
    # root = Node()
    # print(root.child['a'])

    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    obj.insert('app')
    print(obj.search('app'))
