"""
obs
  by i, j, k, extract 2 subarrays
  0 ^ x = x
  x ^ x = 0

arr: [2,3,1,6,7]
bin: [010, 011, 001, 110, 111]
prefix xor: [000, 010, 001, 000, 110, 001]
index:      [0    1     2    3    4    5]

(0, 2, 2)
curr prefix xor = prev prefix xor

(2, 4, 4)
curr prefix xor  = prev prefix xor

(0, 1, 2)
[2], [3, 1]
3: 11
1: 01
3 ^ 1 = 10: 2
[2]: 10, [3, 1]: 10
curr prefix xor: 000, 000 ^ prev prefix xor: 010 = 010
curr xor ^ prev xor = prev xor

(2, 3, 4)
[1], [6, 7]
1: 01
6: 110
7: 111
6 ^ 7 = 001: 1
[1]: 001, [6, 7]: 001
curr xor ^ prev xor = curr xor
"""

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """Prefix"""
        prefix_xor = 0
        prefix_xors = [prefix_xor]
        for i in range(len(arr)):
            prefix_xor ^= arr[i]
            prefix_xors.append(prefix_xor)

        ans = 0

        for start in range(len(prefix_xors)):

            for end in range(start + 1, len(prefix_xors)):

                # If the prefix XOR values at indices start and end are equal, it means the XOR of elements between start and end (excluding start and end) is 0
                if prefix_xors[start] == prefix_xors[end]:
                    # end - start + 1 is the length of the section a + b
                    # use start for i, end for k,
                    # end - start - 1 is the number of position we can put j
                    # so we have that number of pairs for triplets
                    ans += end - start - 1

        return ans

    def countTriplets2(self, arr: List[int]) -> int:
        """Brute force"""
        ans = 0

        for start in range(len(arr) - 1):

            xor_a = 0

            for mid in range(start + 1, len(arr)):

                xor_a ^= arr[mid - 1]

                xor_b = 0

                for end in range(mid, len(arr)):

                    xor_b ^= arr[end]

                    if xor_a == xor_b:
                        ans += 1

        return ans

    def countTriplets1(self, arr: List[int]) -> int:
        prefix_xor = 0
        prefix_xors = [prefix_xor]
        for i in range(len(arr)):
            prefix_xor ^= arr[i]
            prefix_xors.append(prefix_xor)

        print([bin(p) for p in prefix_xors])
        print(prefix_xors)

        ans = 0

        for i in range(len(prefix_xors)):
            for j in range(i + 1, len(prefix_xors)):

                # Case 1: subarray a and b both 1 length array
                if prefix_xors[j] == prefix_xors[i]:
                    ans += 1

                # Case 2:
                elif (prefix_xors[j] ^ prefix_xors[i]) == prefix_xors[j]:
                    ans += 1

        return ans
