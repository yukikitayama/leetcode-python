from typing import List


class Solution:
    # Divide and conquer function
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)

        # Base case
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        # Divide
        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        # Combine
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):

        n_l = len(left)
        n_r = len(right)

        p_l = 0
        p_r = 0

        curr_y = 0
        left_y = 0
        right_y = 0

        def update_output(x, y):

            # Skyline change is not vertical
            if not output or output[-1][0] != x:
                output.append([x, y])
            # Skyline change is vertical
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            while p < n:
                x, y = lst[p]
                p += 1
                # Heigh change
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        output = []

        while p_l < n_l and p_r < n_r:
            point_l = left[p_l]
            point_r = right[p_r]

            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1

            else:
                x, right_y = point_r
                p_r += 1

            max_y = max(left_y, right_y)

            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # There's only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # There's only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(Solution().getSkyline(buildings))
