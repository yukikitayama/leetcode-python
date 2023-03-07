from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        for i in range(len(words)):

            for j in range(len(words[i])):

                if (
                    # If vertical is longer and length doesn't match
                    j >= len(words)
                    # If horizontal is longer and length doesn't match
                    or i >= len(words[j])
                    # If a character doesn't match
                    or words[i][j] != words[j][i]
                ):
                    return False

        return True


