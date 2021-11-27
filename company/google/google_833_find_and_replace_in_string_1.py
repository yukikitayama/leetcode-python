from typing import List
import pprint


class Solution:
    def findReplaceString(self,
                          s: str,
                          indices: List[int],
                          sources: List[str],
                          targets: List[str]) -> str:
        index_to_tuple_source_and_target = {
            index: (source, target) for index, source, target in zip(indices, sources, targets)
        }
        # pprint.pprint(index_to_tuple_source_and_target)

        index = 0
        result = ''

        while index < len(s):
            if index in index_to_tuple_source_and_target \
                    and s[index:].startswith(index_to_tuple_source_and_target[index][0]):
                result += index_to_tuple_source_and_target[index][1]
                # we need to skip by the length of source if we replace it to go to the next source
                index += len(index_to_tuple_source_and_target[index][0])
            else:
                result += s[index]
                index += 1

        return result


"""
Time complexity
Let n be the length of s, and m be the length of indices
O(m) to make a dictionary, and O(n) to while loop, so O(n + m)

Space complexity
O(m) for dictionary
"""


s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print(Solution().findReplaceString(s, indices, sources, targets))
