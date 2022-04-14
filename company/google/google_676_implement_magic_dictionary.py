"""
- *?

"""


from typing import List
import collections


class MagicDictionary:
    def __init__(self):
        self.words = None
        self.counter = None

    def candidate(self, word):
        candidates = []
        for i in range(len(word)):
            # + 1 to skip by '*'
            candidates.append(word[:i] + '*' + word[i + 1:])
        return candidates

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)

        candidates = []
        for word in dictionary:
            candidates.extend(self.candidate(word))

        self.counter = collections.Counter(candidates)

        print(self.counter)

    def search(self, searchWord: str) -> bool:
        for candidate in self.candidate(searchWord):
            if (
                # If searchWord already exist in dictionary, if candidate is more than 1,
                # we can change a character to modify it to another word in dictionary
                # so we are permitted to change exactly one word
                self.counter[candidate] > 1 or
                # searchWord not in self.words because we need to change exactly one word
                # If the searchWord already exist in words, not allowed
                self.counter[candidate] == 1 and searchWord not in self.words
            ):
                return True
        return False


if __name__ == '__main__':
    obj = MagicDictionary()
    dictionary = ['hello', 'hallo', 'leetcode']
    obj.buildDict(dictionary)
    print(obj.search('hello'))  # True
    print(obj.search('hhllo'))  # True
    print(obj.search('hell'))  # False
    print(obj.search('leetcoded'))  # False
    print()

