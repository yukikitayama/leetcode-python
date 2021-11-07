"""
- Count for every char in s
- Think about how many ways to be found as a unique char
- count and sum

- A(XA, AX(A
- A)XXA, AX)XA, AXX)A
- In total, A(XA)XXA, A(XAX)XA, A(XAXX)A, AX(A)XXA, AX(AX)XA, AX(AXX)A
  - 6 ways to make the second A a unique character in a substring

#####################

s: 'XAXAXXAX'

- XA
  - There are two possibilities to place ), but not places to place (

- XAX
  - (X)AX, (XA)X

- XAXA
  - Opening, (XA, X(A
  - Closing, )XA, X)A
  - (XA)XA, (XAX)A, X(A)XA, X(AX)A

...

- i: 7, c: x
  - XAXAXXAX
    - Opening, j - k, X(XAX
    - Closing, i - j, X)AX, XA)X
    - X(X)AX, X(XA)X
"""


import string
import pprint


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Alphabet: [previous index, current index]
        # Possibilities to place ) is between previous index and current index
        # Possibilities to place ( is before previous index
        # Initializing to -1
        index = {c: [-1, -1] for c in string.ascii_uppercase}

        # print(f'index: {index}')
        # pprint.pprint(index)

        res = 0

        # Check how many substring possible to make the previous c unique
        for i, c in enumerate(s):

            k, j = index[c]

            print(f'i: {i}, c: {c}, k: {k}, j: {j}')

            # i: current index, j: last index, k: second last index
            # To make the current c between j and i unique,
            # i - j is the number of possibilities of closing brackets )
            # j - k is the number of possibilities of opening brackets (
            # Multiplication of number of opening brackets and closing brackets
            # which make a previous c unique in substring
            res += (i - j) * (j - k)
            print(f'  res += {(i - j) * (j - k)}')

            print(f'    i - j: {i - j}, j - k: {j - k}, '
                  f'(i - j) * (j - k): {(i - j) * (j - k)}')

            index[c] = [j, i]

            print(f'      index[{c}]: [{j}, {i}]')
            print()

        # pprint.pprint(index)

        # Above iteration always check previous c,
        # so the final appearing c in s is not added to answer
        for c in index:
            k, j = index[c]
            # When an alphabet didn't appear in s
            # it has k: -1, and j: -1
            # so (j - k): -1 + 1 = 0, no contribution
            res += (len(s) - j) * (j - k)

        return res



s = "ABC"
# s = "ABA"
# s = "LEETCODE"
s = 'XAXAXXAX'
print(Solution().uniqueLetterString(s))
