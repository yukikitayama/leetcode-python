"""
- Start: 1:23
- End: 1:45
- Solved: 1
- Saw solution: 0


Idea
- Hashmap with key abbreviation and value a set of words
  - Set because when dictionary is ['a', 'a'], isUnique('a') needs to return True
"""


from typing import List
import collections


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbr_to_word_list = collections.defaultdict(set)
        for word in dictionary:
            abbreviation = self.get_abbreviation(word)
            self.abbr_to_word_list[abbreviation].add(word)

    def isUnique(self, word: str) -> bool:
        abbreviation = self.get_abbreviation(word)

        # print(f'abbreviation: {abbreviation}')
        # print(1, abbreviation in self.abbr_to_word_list)
        # print(2, len(self.abbr_to_word_list[abbreviation]) == 1)
        # print(3, self.abbr_to_word_list[abbreviation][0] == word)

        if abbreviation not in self.abbr_to_word_list:
            # print('if')
            return True
        elif (
                abbreviation in self.abbr_to_word_list
                and len(self.abbr_to_word_list[abbreviation]) == 1
                and next(iter(self.abbr_to_word_list[abbreviation])) == word
        ):
            # print('elif')
            return True
        else:
            # print('else')
            return False

    def get_abbreviation(self, word: str) -> str:
        if len(word) < 3:
            return word
        else:
            count = len(word[1:-1])
            return word[0] + str(count) + word[-1]


"""
Complexity
- Time
  - Constructor is O(n)
  - isUnique() is O(1)
- Space is O(n) 
"""


dictionary = ["deer", "door", "cake", "card"]
obj = ValidWordAbbr(dictionary)
print(obj.abbr_to_word_list)
print(obj.isUnique('dear'))  # F
print(obj.isUnique('cart'))  # T
print(obj.isUnique('cane'))  # F
print(obj.isUnique('make'))  # T
print(obj.isUnique('cake'))  # T

# dictionary = ['a', 'a']
# obj = ValidWordAbbr(dictionary)
# print(obj.abbr_to_word_list)
# print(obj.isUnique('a'))  # True
