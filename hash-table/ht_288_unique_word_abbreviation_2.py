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

        # True if there is no word in dictionary
        # whose abbreviation is equal to word's abbreviation.
        if abbreviation not in self.abbr_to_word_list:
            return True

        # True if For any word in dictionary whose abbreviation is
        # equal to word's abbreviation, that word and word are the same.
        elif (
                abbreviation in self.abbr_to_word_list
                and len(self.abbr_to_word_list[abbreviation]) == 1
                and next(iter(self.abbr_to_word_list[abbreviation])) == word
        ):
            return True
        else:
            return False

    def get_abbreviation(self, word: str) -> str:
        if len(word) < 3:
            return word
        else:
            # Python list end slice is exclusive,
            # so :-1 means not including the last character
            count = len(word[1:-1])
            return word[0] + str(count) + word[-1]


"""
Idea
- Hashmap with key abbreviation and value a set of words
  - Set because when dictionary is ['a', 'a'], isUnique('a') needs to return True
  - If you use list as value of the hashmap, length of the value is 2 above, 
    so it cannot return True in isUnique()

Complexity
- Time
  - Let n be the length of the dictionary
  - Constructor is O(n)
  - isUnique() is O(1)
  - get_abbreviation() is O(1)
- Space is O(n) for the hashmap 
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
