"""
Hashmap
  k: s
  v: t
Iterate s
  if s char not in hashmap
    create new s: t
  if s char in hashmap
    check if hashmap value is equal to t char
      if not
        return false
return true

s: "badc", t: "baba", F
  b: b
  a: a
  d: b
  c: a

Compare counter
"""

import collections


class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(s)
        cc_s = collections.defaultdict(int)
        for k, v in counter_s.items():
            cc_s[v] += 1
        counter_t = collections.Counter(t)
        cc_t = collections.defaultdict(int)
        for k, v in counter_t.items():
            cc_t[v] += 1
        if cc_s == cc_t:
            return True
        else:
            return False

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = collections.defaultdict(str)
        t_to_s = collections.defaultdict(str)

        for i in range(len(s)):

            # New pair
            if s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]

            elif s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
                return False

        return True
