"""
hash function?
  word -> order

order
  character to integer
    h: 0
    l: 1

Replace each word and sort the list
Convert word by place at order to place at true alphabet

abcdefg
hlabcde

hello -> agbb
leetcode -> bgg


{"h": 0}

True
{0: "a"}

Conversion
  create hashmap to iterate order
  create hashmap to iterate a to z
    chr(ord("a")): "a"
    character - ord("a"): 0 to 25

Answer
  Only compare each pair of adjacent words
"""

from typing import List
import collections


class Solution:
    # def isAlienSorted(self, words: List[str], order: str) -> bool:

    #     order_hashmap = collections.defaultdict(int)
    #     for i in range(len(order)):
    #         order_hashmap[order[i]] = i

    #     true_hashmap = collections.defaultdict(str)
    #     for i in range(26):
    #         character = chr(ord("a") + i)
    #         true_hashmap[i] = character

    #     true_to_original = collections.defaultdict(str)
    #     converted = []

    #     for word in words:

    #         curr = []

    #         for ch in word:
    #             i = order_hashmap[ch]
    #             true_char = true_hashmap[i]
    #             curr.append(true_char)

    #         converted.append("".join(curr))
    #         true_to_original["".join(curr)] = word

    #     converted.sort()

    #     print(converted)

    #     ans = []
    #     for conv in converted:
    #         ans.append(true_to_original[conv])

    #     for i in range(len(words)):
    #         if words[i] != ans[i]:
    #             return False
    #     return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        character_to_order = collections.defaultdict(int)
        for i in range(len(order)):
            character_to_order[order[i]] = i

        for i in range(len(words) - 1):

            curr_word = words[i]
            next_word = words[i + 1]

            for j in range(len(curr_word)):

                # If all characters so far are all same, but next_word is shorter than curr_word
                if j >= len(next_word):
                    return False

                if curr_word[j] != next_word[j]:

                    if character_to_order[curr_word[j]] > character_to_order[next_word[j]]:
                        return False

                    # Different character now, but current character of curr_word is smaller, so it's sorted
                    # No need to compare more
                    else:
                        break

        return True
