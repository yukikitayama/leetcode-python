"""
A word is considered valid if:

It contains a minimum of 3 characters.
It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
"""


class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        found_vowel = False
        found_consonant = False

        for i in range(len(word)):

            if not word[i].isalnum():
                return False

            if word[i].lower() in "aeiou":
                found_vowel = True

            if word[i].isalpha() and word[i].lower() not in "aeiou":
                found_consonant = True

        print(found_vowel, found_consonant)

        if found_vowel and found_consonant:
            return True
        else:
            return False