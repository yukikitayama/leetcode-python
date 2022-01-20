"""
- Create Trie from dictionary
- For each word in sentence, find prefix from Trie word
  - If search fail, use the word itself, not modification
"""


from typing import List
import collections
import functools


class Solution:
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in dictionary:
            functools.reduce(dict.__getitem__, root, trie)[END] = root
        # This creates a Trie like
        # 'cat',
        # {
        #     'c': {
        #         'a': {
        #             't': {
        #                 True: 'cat'
        #             }
        #         }
        #     }
        # }

        # print(trie.keys())
        # print(trie['c'].keys())
        # print(trie['c']['a'])
        # print(trie['c']['a']['t'])

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]

            return cur.get(END, word)

        return ' '.join(map(replace, sentence.split()))


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.child[c]
        curr.is_word = True

    def search_prefix(self, prefix) -> str:
        curr = self.root

        prefix = []

        for c in prefix:
            prefix.append(c)
            if curr.is_word:
                return ''.join(prefix)

            if c not in curr:
                return ''
            curr = curr.child[c]


class SolutionFail:
    def replaceWords(self, dictionary: List[str], sentence: str):
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        # print(trie.root.child.keys())
        # print(trie.root.child['c'].child.keys())
        # print(trie.root.child['c'].child['a'].child['t'].is_word)

        ans = []

        for word in sentence:
            result = trie.search_prefix(word)
            ans.append(result)

        return ans


if __name__ == '__main__':
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary, sentence))

    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    words = ['abc', 'def']
    for word in words:
        curr = trie
        for c in word:
            curr = curr[c]
        curr['is_word'] = True
        # or
        # curr[True] = word

    print(trie.keys())
    import pprint
    pprint.pprint(trie)