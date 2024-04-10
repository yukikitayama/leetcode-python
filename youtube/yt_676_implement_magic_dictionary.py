"""
Brute force
  N: length of dictionary array
  M: current searchWord
  T: O(NM)
    100 search methods * 100 dictionary length * 100 search word length = 1,000,000
  Bottleneck is iteration of dicrionary array
  T: O(NlogM)


"""

from typing import List


class MagicDictionary:

    def __init__(self):
        self.dictionary = None

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary
        self.dictionary.sort(key=lambda x: (len(x), x))

    def search(self, searchWord: str) -> bool:
        # print(f"searchWord: {searchWord}, self.dictionary: {self.dictionary}")
        for dict_word in self.dictionary:

            if len(dict_word) > len(searchWord):
                return False

            elif len(dict_word) < len(searchWord):
                continue

            # print(f"  dict_word: {dict_word}")

            for i in range(len(searchWord)):
                if (
                        dict_word[:i] == searchWord[:i]
                        and dict_word[i + 1:] == searchWord[i + 1:]
                        and dict_word[i] != searchWord[i]
                ):
                    return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)