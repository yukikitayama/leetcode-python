from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)

        def shift_and_count(x_shift, y_shift, M, R):
            """

            :param x_shift:
            :param y_shift:
            :param M: matrix to be moved, both img1 and img2 are used for M. Move M in up-left and up-right
            :param R: matrix for reference
            :return:
            """
            left_shift_count, right_shift_count = 0, 0

            # r_row always starts from 0, but m_row could start between from 0 and from dim
            for r_row, m_row in enumerate(range(y_shift, dim)):
                # r_col always starts from 0, but m_col could start between from 0 and from dim
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        max_overlaps = 0

        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img1, img2))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img2, img1))

        return max_overlaps


"""
Time complexity
O(n**4)

Space complexity
O(1)
"""