
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)

        # x overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        # positive if overlapped
        x_overlap = right - left

        # y overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        area_ab = 0
        if x_overlap > 0 and y_overlap > 0:
            area_ab = x_overlap * y_overlap

        return area_a + area_b - area_ab


class Solution1:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        holizontal_a = abs(ax1 - ax2)
        vertical_a = abs(ay1 - ay2)
        area_a = holizontal_a * vertical_a

        holizontal_b = abs(bx1 - bx2)
        vertical_b = abs(by1 - by2)
        area_b = holizontal_b * vertical_b

        if ax2 <= bx1:
            area_ab = 0
        elif bx2 <= ax1:
            area_ab = 0
        elif ay2 <= by1:
            area_ab = 0
        elif by2 <= ay1:
            area_ab = 0
        elif area_a and area_b:
            holizontal_ab = abs(ax2 - bx1)
            vertical_ab = abs(ay1 - by2)
            area_ab = holizontal_ab * vertical_ab
        else:
            area_ab = 0

        print(f'area_a: {area_a}, area_b: {area_b}, area_ab: {area_ab}')

        ans = area_a + area_b - area_ab

        return ans


if __name__ == '__main__':
    ax1 = -3
    ay1 = 0
    ax2 = 3
    ay2 = 4
    bx1 = 0
    by1 = -1
    bx2 = 9
    by2 = 2
    # 45

    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -2
    by1 = -2
    bx2 = 2
    by2 = 2
    # 16

    ax1 = 0
    ay1 = 0
    ax2 = 0
    ay2 = 0
    bx1 = -1
    by1 = -1
    bx2 = 1
    by2 = 1
    # 4

    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -1
    by1 = -1
    bx2 = 1
    by2 = 1
    # 16

    print(Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))

