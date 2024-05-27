"""
Input: word = "abcde"
Output: "1a1b1c1d1e"

Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"

Simulation
"""


class Solution:
    def compressedString(self, word: str) -> str:

        ans = []

        curr_count = 0
        curr_ch = None

        for i in range(len(word)):

            if word[i] == curr_ch and curr_count < 9:
                curr_count += 1

            elif word[i] == curr_ch and curr_count == 9:
                curr_count = 1
                ans.append("9" + curr_ch)

            elif word[i] != curr_ch:
                if curr_count != 0:
                    ans.append(str(curr_count) + curr_ch)
                curr_ch = word[i]
                curr_count = 1

        ans.append(str(curr_count) + curr_ch)

        return "".join(ans)
