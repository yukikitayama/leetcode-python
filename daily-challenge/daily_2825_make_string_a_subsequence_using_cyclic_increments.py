class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p2 = 0
        for p1 in range(len(str1)):
            if p2 < len(str2) and (
                str1[p1] == str2[p2]
                or ord(str1[p1]) + 1 == ord(str2[p2])
                or ord(str1[p1]) - 25 == ord(str2[p2])
            ):
                p2 += 1
        return p2 == len(str2)