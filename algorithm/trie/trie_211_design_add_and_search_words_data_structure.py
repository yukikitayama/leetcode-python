import collections


class WordDictionary:
    def __init__(self):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            curr = curr[c]
        curr[True] = word

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, ch in enumerate(word):

                if ch not in node:
                    # If '.', we need to explore all possible paths at each . level
                    if ch == '.':
                        for x in node:
                            if x is not True and search_in_node(word[i + 1:], node[x]):
                                return True
                    return False

                else:
                    node = node[ch]

            return True in node

        curr = self.trie
        return search_in_node(word, curr)


if __name__ == '__main__':
    obs = WordDictionary()
    obs.addWord('bad')
    obs.addWord('dad')
    obs.addWord('mad')
    print(obs.search('pad'))
    print(obs.search('bad'))
    print(obs.search('.ad'))
    print(obs.search('b..'))

