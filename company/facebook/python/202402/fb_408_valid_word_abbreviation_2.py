"""
pointer to abbr
  when curr is character,
    increment abbr pointer
    increment word pointer
  when curr is digit, move pointer until the end of digits
    move abbr pointer one after the digit
    move word pointer by the digit
  if two pointers point different return False
if finish iteration, return True
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pointer = 0
        abbr_pointer = 0

        # num from abbr might move word pointer out of word length
        while word_pointer < len(word) and abbr_pointer < len(abbr):

            if abbr[abbr_pointer].isdigit():

                # Leading zero isn't allowed
                if abbr[abbr_pointer] == "0":
                    return False

                num = 0

                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    num = num * 10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1
                # Here abbr_pointer points at character
                word_pointer += num
                # After this word_pointer also points at character

            else:
                if word[word_pointer] == abbr[abbr_pointer]:
                    word_pointer += 1
                    abbr_pointer += 1
                else:
                    return False

        print(word_pointer, abbr_pointer)

        # word: "a", abbr: "2", word supposed to have 2 characters, but the word doesn't have it
        # Bascially after moving word pointer by number in abbr, both pointers need to be at the same index
        # and if abbreviation is correct, after iteration, pointers should be at the length of strings
        return word_pointer == len(word) and abbr_pointer == len(abbr)
