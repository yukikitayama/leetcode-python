"""
a ^ a = 0
"""


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range(len(pref) - 1, 0, -1):
            pref[i] = pref[i] ^ pref[i - 1]
        return pref

    def findArray1(self, pref: List[int]) -> List[int]:
        ans = []

        ans.append(pref[0])

        for i in range(1, len(pref)):

            num = pref[i] ^ pref[i - 1]
            ans.append(num)

        return ans