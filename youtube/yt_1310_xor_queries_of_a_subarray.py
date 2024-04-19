"""
[0001, 0011, 0100, 1000]
prefix XOR
[0000, 0001, 0010, 0110, 1110]

[0, 1], 0010
[1, 2], 0111, prefix_xor[2] XOR prefix_xor[1 - 1]
[0, 3], 1110 = 2**3 + 2**2 + 2**1 = 8 + 4 + 2 = 14

Ans
  If we have (a^b^c) ^ (a), we get (b^c)
  Because x ^ x = 0, x ^ 0 = x, and we can change the order to apply XOR
  So (a^b^c) ^ (a) = a^b^c^a = a^a^b^c = 0^b^c = b^c
"""

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]

        for i in range(len(arr)):
            prefix_xor.append(prefix_xor[-1] ^ arr[i])

        # for p in prefix_xor:
        #     print(p, bin(p))

        ans = []

        for query in queries:
            right_xor = prefix_xor[query[1] + 1]
            left_xor = prefix_xor[query[0]]

            ans.append(right_xor ^ left_xor)

        return ans
