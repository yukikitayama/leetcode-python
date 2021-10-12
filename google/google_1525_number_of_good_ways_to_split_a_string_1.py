from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        # Empty counter is initialized
        left_counter = Counter()
        right_counter = Counter(s)

        # print(f'left_counter: {left_counter}, right_counter: {right_counter}')

        res = 0

        for c in s:

            left_counter[c] += 1
            right_counter[c] -= 1

            if right_counter[c] == 0:
                del right_counter[c]

            # print(f'c: {c}, left_counter: {left_counter}, right_counter: {right_counter}')

            if len(left_counter) == len(right_counter):
                res += 1

        return res


"""
Use two counter dictionaries. One is initially empty and the other is counted for all the characters in s
As we iterate each character in s, we increment empty counter and decrement the full counter.
Important thing is that, when we have 0 in the initially full counter, need to delete the key and value,
because eventually we will compare the number of keys in each dictionary to know how many distinct characters are there.
Distinct characters do not need to be the same. Just the number of distinct characters.

Time complexity
Let n be the length of s. O(n) to do for loop.

Space complexity
O(26) because we will only have lowercase English letter, so it's not n
"""


s = "aacaba"
s = "abcd"
# s = "aaaaa"
s = "acbadbaada"
print(Solution().numSplits(s))
