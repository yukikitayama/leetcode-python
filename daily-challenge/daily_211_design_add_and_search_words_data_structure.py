class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        # At the end, mark as this is word
        # The final character as a key has a value of dictionary
        # The value is {'$': True}
        curr['$'] = True

    def search(self, word: str) -> bool:

        def search_curr(word, node):
            for i, c in enumerate(word):
                if c not in node:
                    if c == '.':
                        for key in node:
                            if key != '$' and search_curr(word[i + 1:], node[key]):
                                return True
                    return False
                else:
                    node = node[c]

            # Here finished iterating all the characters
            # node is {'$': True} or empty dictionary
            return '$' in node

        return search_curr(word, self.trie)


if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('bad')
    print(obj.trie)
