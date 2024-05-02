"""
aba
  a: 2
  b: 1
  1 odd

ab
  a: 1
  b: 1
  2 odds

Counter hashmap
Two pointers

Ans
  Parity: whether the count of a letter in a word is even or odd
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        # k: bitmask, v: freq of the bitmask
        freq = {}

        # ?
        freq[0] = 1

        mask = 0

        ans = 0

        for ch in word:

            bit_position = ord(ch) - ord("a")

            mask ^= (1 << bit_position)

            if mask in freq:

                # If previously seen mask is equal to current mask
                # then prev ^ curr = 0, meaning all characters are even counts
                ans += freq[mask]
                freq[mask] += 1

            else:
                freq[mask] = 1

            for odd_ch_position in range(10):

                # prev: abbc (101), curr: abbbc (111), find b
                # removed: 110, 101, 011 by XOR 1 to each bit in curr
                removed = mask ^ (1 << odd_ch_position)
                if removed in freq:
                    ans += freq[removed]

        return ans