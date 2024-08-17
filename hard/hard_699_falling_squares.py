from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        qans = [0] * len(positions)

        for i, (left, size) in enumerate(positions):

            right = left + size

            # size is height as well as width
            # This accumulates height
            qans[i] += size

            for j in range(i + 1, len(positions)):

                left2, size2 = positions[j]
                right2 = left2 + size2

                # Intersect
                if left2 < right and left < right2:
                    qans[j] = max(qans[i], qans[j])

        # print(qans)

        ans = [qans[0]]
        for i in range(1, len(qans)):
            ans.append(max(ans[-1], qans[i]))

        return ans