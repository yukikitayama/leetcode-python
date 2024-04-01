"""
Palindrome
  Only even counts characters e.g. abba
  One odd count abd even counts characters e.g. abcba, abbba
  If multiple odds, not palindrome, e.g. abca

Hashmap
  k: character
  v: counts
  e.g. s: "annabelle", k: 2
    a: 2,
    b: 1,
    e: 2,
    l: 2,
    n: 2
  e.g. s: "leetcode", k: 3
    c: 1,
    d: 1,
    e: 3,
    l: 1,
    o: 1,
    t: 1

T: O(N)
S: O(26) = O(1)
"""

import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Edge
        if len(s) < k:
            return False

        counter = collections.Counter(s)
        num_odd = 0
        for ch, v in counter.items():
            if v % 2 != 0:
                num_odd += 1

        if num_odd <= k:
            return True
        else:
            return False
