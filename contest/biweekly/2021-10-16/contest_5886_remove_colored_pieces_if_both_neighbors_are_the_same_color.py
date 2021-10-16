"""

"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        A = [0] * len(colors)
        B = [0] * len(colors)

        for i in range(1, len(colors) - 1):
            if (colors[i] == 'A'
                and colors[i - 1] == 'A'
                and colors[i + 1] == 'A'):
                A[i] = 1

            if (colors[i] == 'B'
                and colors[i - 1] == 'B'
                and colors[i + 1] == 'B'):
                B[i] = 1

        # print(f'A: {A}')
        # print(f'B: {B}')

        if sum(A) > sum(B):
            return True

        if sum(A) <= sum(B):
            return False


# colors = "AAABABB"  # True
colors = "AA"  # False
# colors = "ABBBBBBBAAA"  # False
print(Solution().winnerOfGame(colors))
