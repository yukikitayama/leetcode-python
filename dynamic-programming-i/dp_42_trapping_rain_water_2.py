from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        st = []

        while current < len(height):

            while len(st) != 0 and height[current] > height[st[-1]]:
                top = st[-1]
                st.pop()

                if len(st) == 0:
                    break

                distance


"""
"""

