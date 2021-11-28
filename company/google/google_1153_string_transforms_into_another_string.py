class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:

        if str1 == str2:
            return True

        dp = {}

        for i, j in zip(str1, str2):
            # print(f'i: {i}, j: {j}, dp.setdefault(i, j): {dp.setdefault(i, j)}')

            value = dp.setdefault(i, j)

            print(f'i: {i}, j: {j}, dp.setdefault({i}, {j}): {value}')

            # setdefault() returns the value of the first argument key,
            # If it doesn't exist, it inserts the key with the second argument as value, returns the same value
            # If the key exists, it returns the value
            if value != j:
                return False

            print(dp)

        # Why this, instead of return True?
        return len(set(str2)) < 26


"""
a -> b -> c
mapping: {a: b, b: c}. We don't need key c. Length of dict is 2

a -> b -> c -> a
mapping: {a: b, b: c, c: a}. Length of dict is 3

In both case, at least one character from graph is not used.

I don't understand why the below case needs to be False
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "bcdefghijklmnopqrstuvwxyza"
"""


# True
str1 = "aabcc"
str2 = "ccdee"

# True
str1 = 'aabccf'  # ccdeeb
str2 = 'ccdeeb'

str1 = 'aabcce'
str2 = 'ccdeea'

# str1 = "leetcode"
# str2 = "codeleet"
# str1 = "abcdefghijklmnopqrstuvwxyz"
# str2 = "bcdefghijklmnopqrstuvwxyza"
print(Solution().canConvert(str1, str2))
