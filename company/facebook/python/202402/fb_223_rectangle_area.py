"""
6 * 4 = 24
9 * 3 = 27
3 * 2 = 6
24 + 27 - 6 = 51 - 6 = 45

Sum two rectangle and subtract overlap if overlap
When it doesn't overlap
  Vertically not overlap
    (ax1, ay1) is higher than or equal to (bx2, by2)
    (bx1, by1) is higher than or equal to (ax2, ay2)
  Holizontally not overlap
    (ax2, ay2) is smaller than or equal to (bx1, by1)
    (bx2, by2) is smaller than or equal to (ax1, ay1)


"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def compute_area(x1, y1, x2, y2):
            return abs(x1 - x2) * abs(y1 - y2)

        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)

        # Horizontally not overlap or vertically not overlap
        if cx2 <= cx1 or cy2 <= cy1:
            area_a = compute_area(ax1, ay1, ax2, ay2)
            area_b = compute_area(bx1, by1, bx2, by2)
            return area_a + area_b
        else:
            area_a = compute_area(ax1, ay1, ax2, ay2)
            area_b = compute_area(bx1, by1, bx2, by2)
            area_c = compute_area(cx1, cy1, cx2, cy2)
            return area_a + area_b - area_c
