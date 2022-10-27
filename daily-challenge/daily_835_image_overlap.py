from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        dim = len(img1)

        def shift_and_count(x_shift, y_shift, M, R):
            """Shift M to up-left or up-right, M moves, R doesn't move"""
            left_shift_count = 0
            right_shift_count = 0

            # r_row always starts with 0
            # m_row starts with y_shift
            # r_ means reference, m_ means move
            # As starting point moves more, for loop shrink and doesn't cover entire matrix,
            # but it doesn't matter because the area doesn't cover is filled with 0, and we don't count 0,
            # so we can ignore
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):

                    # Move M to left
                    if M[m_row][m_col] and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    # Move R to left, meaning moving M to right
                    if M[m_row][r_col] and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        ans = 0

        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                ans = max(ans, shift_and_count(x_shift, y_shift, img1, img2))
                # By exchanging image 1 and 2, compute the other half that we couldn't cover by the above operation
                ans = max(ans, shift_and_count(x_shift, y_shift, img2, img1))

        return ans
