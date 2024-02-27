"""
Hashmap
  k: tuple of diff between each character and first character
    abc -> (0, 1, 2)
  v: list of strings
"""

from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        k_to_strings = collections.defaultdict(list)

        for string in strings:

            # Convert string to key
            key = []
            for i in range(len(string)):
                diff = (ord(string[i]) - ord(string[0])) % 26
                key.append(diff)

                # Add the key and string to hashmap
            k_to_strings[tuple(key)].append(string)

        # print(k_to_strings)

        # Return values
        return k_to_strings.values()

        # # Create a hash value
        # def get_hash(string: str):
        #     key = []
        #     for a, b in zip(string, string[1:]):
        #         key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
        #     return ''.join(key)

        # # Create a hash value (hash_key) for each string and append the string
        # # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        # groups = collections.defaultdict(list)
        # for string in strings:
        #     hash_key = get_hash(string)
        #     # print(string, hash_key)
        #     groups[hash_key].append(string)

        # # Return a list of all of the grouped strings
        # return list(groups.values())