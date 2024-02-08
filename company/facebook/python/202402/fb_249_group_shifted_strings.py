"""
Need a way to represent strings such that the ones belonging to the same shifting sequence have the same value

Create hash function

Convert a string to array of integers
  integer for distance of each character to the first character
    abc = [0, 1, 2], xyz = [0, 1, 2],
    trouble, zab = [0, 1, 2], ord('a') - ord('z') % 26
    az
    ba

Hashmap
  Key: array of indices
  Value: list of strings

Convert hashmap to list of list as answer
"""

from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        groups = collections.defaultdict(list)

        for i in range(len(strings)):

            string = strings[i]
            chars = [ch for ch in string]
            # b - a = 1, z - y = 1
            # (ord(a) - ord(z)) % 26 = (-25) % 26 = 1
            key = [(ord(ch) - ord(chars[0])) % 26 for ch in chars]

            groups[tuple(key)].append(string)

        print(groups)

        return groups.values()


if __name__ == "__main__":

    print(ord("z") - ord("a"))
    print(ord("a") - ord("z"))
    print((ord("a") - ord("z")) % 26)
    print(-1 % 26)  # 25
    print(-25 % 26)  # 1

    str1 = "az"
    str2 = "ba"

