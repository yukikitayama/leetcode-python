"""
- Start: 12:42
- End 1:02
- Solved: 0
- Saw solution: 1

Idea
- Find a max character in a string
  - Calculate the distance between the max character and other characters
    - e.g. 'abc', max character: 'c', distances to max character: 2, 1, 0
    - e.g. 'bcd', max character: 'd', distances to max character: 2, 1, 0
"""


from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        distances_to_string_list = collections.defaultdict(list)

        for string in strings:
            max_character = max(string, key=ord)
            # %
            distances = tuple([ord(max_character) - ord(char) for char in string])
            print(f'string: {string}, distances: {distances}')
            distances_to_string_list[distances].append(string)

        print(distances_to_string_list)

        ans = []
        for item in distances_to_string_list.values():
            ans.append(item)
        return ans


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(Solution().groupStrings(strings))

