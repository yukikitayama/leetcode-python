"""
Sliding window
"""

from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        ans = []

        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i + 1] == "+":
                copied = [c for c in currentState]
                copied[i] = "-"
                copied[i + 1] = "-"
                ans.append("".join(copied))

        return ans
