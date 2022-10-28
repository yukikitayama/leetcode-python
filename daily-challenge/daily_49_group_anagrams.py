from typing import List
import collections


"""
- Categorize by character counts
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for str_ in strs:

            count = [0] * 26

            for ch in str_:

                count[ord(ch) - ord('a')] += 1

            ans[tuple(count)].append(str_)

        return ans.values()


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for str_ in strs:
            ans[''.join(sorted(str_))].append(str_)

        return list(ans.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))
