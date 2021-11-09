"""
Idea
- No need count the number of character,
  - use set
- Initialize ans to an empty list
- Iterate each puzzle in puzzles
  - Initialize counter to 0
  - Iterate each word in words
    - Iterate each character in the current word
      - If all the characters are in the current word
        - Set a boolean True
    - If word contains the first letter of the current puzzle
      and if the boolean True
      - Increment counter by one
  - Append the counter to ans

Complexity
- Time is O(n^3) for the 3 nested for loops
- Space is (n^2) for set

- Take out iterate each character in word code out of the nested for loops
"""


def bitmask(word):
    mask = 0
    for letter in word:
        # Distance between a and current letter
        dist = ord(letter) - ord('a')
        # Get bit position
        bit_position = 1 << dist
        # Incrementally fill the bit position by OR to the current mask
        mask = mask | bit_position
    return mask


# word = 'abc'  # 111
word = 'ace'  # 10101
mask = bitmask(word)
print(mask)
print(bin(mask))

mask = 0
tmp = (ord(word[0]) - ord('a'))
print(tmp)
print(1 << tmp)
print(bin(1 << tmp))
mask = mask | (1 << tmp)
print(mask)
tmp = (ord(word[1]) - ord('a'))
print(tmp)
print(1 << tmp)
print(bin(1 << tmp))  # 100
"""
Assignment operator
|=, x |= 3, x = x | 3

Bitwise operator
|, OR, 1 if one of two bits is 1
<<, zero fill left shift, shift left by pushing zeros in from the right,
  and let the leftmost bits fall off
"""


from typing import List
import collections
import pprint


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def bitmask(word):
            mask = 0
            for letter in word:
                # Distance between a and current letter
                dist = ord(letter) - ord('a')
                # Get bit position
                bit_position = 1 << dist
                # Incrementally fill the bit position by OR to the current mask
                mask = mask | bit_position
            return mask

        word_count = collections.Counter(bitmask(word) for word in words)

        for k, v in word_count.items():
            print(f'{bin(k)}: {v}')

        ans = []

        for puzzle in puzzles:

            print(f'puzzle: {puzzle}')

            # Get bitmask for the first letter of the current puzzle
            # by pushing 1 to the letter bit position
            first = 1 << (ord(puzzle[0]) - ord('a'))

            print(f'bin(first): {bin(first)}')

            # Why do you have to do this?
            # Even if here word_count[first] and the below while loop has word_count[submask | first],
            # there's no double count because submask is from mask, which is bitmask(puzzle[1:]),
            # excluding the first letter, and if puzzle[1:] has no letter, mask is 0, so submask is 0
            # and it won't run the while loop to increment count
            count = word_count[first]

            print(f'count: {count}')

            # 1:?
            # When making submask in the below while loop, every submask needs to have
            # the first letter position to 1-bit. That's why submask starts from 1: letter,
            # but in the while loop it makes sure to have 1-bit in first letter in every submask
            # by submask | first
            # Convert the current puzzle to bitmask of each letter
            mask = bitmask(puzzle[1:])

            print(f'bin(mask): {bin(mask)}')

            submask = mask

            # While loop stops when submask is 0
            # 0 submask means empty word, so we cannot compare puzzle and word
            # so we don't have to count
            while submask:
                count += word_count[submask | first]

                # submask - 1 and AND mask gives us all the possible bitmasks
                # which are subset of mask
                # e.g. mask: 1001, subset: 1001, 1000, 0001, 0000
                submask = (submask - 1) & mask

            ans.append(count)

        return ans


words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# puzzles = ['ace', "aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(Solution().findNumOfValidWords(words, puzzles))





