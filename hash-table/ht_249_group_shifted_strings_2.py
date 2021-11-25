"""
Idea
- A tuple of distances between characters is key of hashmap and value is a list of the strings
- az and ba need to be the same
  - 'z' - 'a' = ord('z') - ord('a') = 122 - 97 = 25
  - ord('a') - ord('b') = 97 - 80 = -1
  - Add 26 to make both positive and modulo by 26 to make them inside the 26 range
    - 25 + 26 = 51, 51 % 26 = 25
    - -1 + 26 = 25, 25 % 26 = 25
"""


from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        differences_to_string_list = collections.defaultdict(list)

        for string in strings:

            key = tuple()
            # -1 to avoid index out of bound when i+1
            for i in range(len(string) - 1):
                difference = (ord(string[i + 1]) - ord(string[i]) + 26) % 26
                key += (difference,)

            # print(f'string: {string}, key: {key}')

            differences_to_string_list[key].append(string)

        # print(differences_to_string_list)

        ans = []
        for item in differences_to_string_list.values():
            ans.append(item)
        return ans


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(Solution().groupStrings(strings))

