"""

Algorithm
- Make a hashmap from indices, sources and targets
  - Key is index
  - Value is tuple of source and target
- Initialize s iteration index to 0
- Initialize ans to empty string
- While the index is less than the length of s
  - If the current index is in the hashmap and
    the s starting from the current index starts with the current source
    - Append the current target to ans
    - Increment the index by the amount of the current source
  - Otherwise
    - Append the current string in s to ans
    - Increment the index by 1
"""


from typing import List
import pprint


class Solution:
    def findReplaceString(
            self,
            s: str,
            indices: List[int],
            sources: List[str],
            targets: List[str]
    ) -> str:
        index_to_source_target = {
            index: (source, target) for index, source, target in zip(indices, sources, targets)
        }

        # pprint.pprint(index_to_source_target)

        index = 0
        ans = ''

        while index < len(s):

            if index in index_to_source_target and s[index:].startswith(index_to_source_target[index][0]):
                ans += index_to_source_target[index][1]
                index += len(index_to_source_target[index][0])

            else:
                ans += s[index]
                index += 1

            # print(f'index: {index}, ans: {ans}')

        return ans



s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
s = "abcd"
indices = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(Solution().findReplaceString(s, indices, sources, targets))

