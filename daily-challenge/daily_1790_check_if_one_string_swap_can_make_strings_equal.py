"""
hashmap
  first unequal
    s1_to_s2: {b: k}
    s2_to_s1: {k: b}
  second unequal
    if s2_to_s1[s1] == s2 and s1_to_s2[s2] == s1

"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        freq1 = [0] * 26
        freq2 = [0] * 26
        counter = 0
        for i in range(len(s1)):

            if s1[i] != s2[i]:
                counter += 1

                if counter > 2:
                    return False

            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        return freq1 == freq2