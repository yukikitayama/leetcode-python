from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)

        if ns < np:
            return []

        p_count = collections.Counter(p)
        s_count = collections.Counter()

        ans = []

        for i in range(ns):

            s_count[s[i]] += 1

            # To make counter comparison happen, organize the number of key and value in s_count
            if i >= np:
                # Delete the key for comparison
                # i - np + 1 is the start index, so i - np is the outside
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # print(f'p_count: {p_count}, s_count: {s_count}')

            if p_count == s_count:
                # in iteration if becomes True at the end of the anagram
                # so i - np, and + 1 because np is 1-based, but i is 0-based
                ans.append(i - np + 1)

        return ans


if __name__ == '__main__':
    # c1 = collections.Counter('aab')
    # c2 = collections.Counter()
    # print(c1 == c2)  # False
    # c2['a'] = 1
    # c2['b'] = 1
    # print(c1 == c2)  # False
    # c2['a'] = 2
    # print(c1 == c2)  # True
    # c2['c'] = 0
    # print(c1 == c2)  # False
    s = "cbaebabacd"
    p = "abc"
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))
