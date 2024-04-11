"""
Brute force
  Decode
    Decode encoded1
    Decode encoded2
    Create one decode function
      empty array
      for each element, append element[0] by element[1] times
  product empty array
  For each element, compute product and append to the array
  Encode the product array
    empty array as answer
    current index 0
    Iterate array
      counter 1
      while loop
        if next character is the same as current character,
          increment current index
          increment counter
      current increment
      apppend(current number, freq)
  Return
"""

from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []

        p1 = 0
        p2 = 0

        while p1 < len(encoded1) and p2 < len(encoded2):

            val1, freq1 = encoded1[p1]
            val2, freq2 = encoded2[p2]

            prod = val1 * val2
            min_freq = min(freq1, freq2)

            # Use
            encoded1[p1][1] -= min_freq
            if encoded1[p1][1] == 0:
                p1 += 1

            encoded2[p2][1] -= min_freq
            if encoded2[p2][1] == 0:
                p2 += 1

            if not ans:
                ans.append([prod, min_freq])
            elif ans[-1][0] != prod:
                ans.append([prod, min_freq])
            # Updated freq
            else:
                ans[-1][1] += min_freq

        return ans

    def findRLEArray1(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        def decode(encoded):
            ans = []

            for i in range(len(encoded)):
                val, freq = encoded[i]

                for _ in range(freq):
                    ans.append(val)

            return ans

        decoded1 = decode(encoded1)
        decoded2 = decode(encoded2)

        # print(decoded1)
        # print(decoded2)

        # Do products
        products = [d1 * d2 for d1, d2 in zip(decoded1, decoded2)]

        # print(products)

        # Encode
        ans = []
        i = 0
        while i < len(products):
            counter = 1

            while i < len(products) - 1 and products[i] == products[i + 1]:
                i += 1
                counter += 1

            ans.append([products[i], counter])

            i += 1

        return ans
