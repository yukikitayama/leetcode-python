"""
T: O(N)
S: O(N)
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)

        # Invalid for at most once
        if len(diff_indices) > 2:
            return False
        # Cannot swap
        elif len(diff_indices) == 1:
            return False
        # No need to swap
        elif len(diff_indices) == 0:
            return True
        elif len(diff_indices) == 2:
            # Cannot swap
            if s1[diff_indices[0]] != s2[diff_indices[1]] or s1[diff_indices[1]] != s2[diff_indices[0]]:
                return False
            else:
                return True