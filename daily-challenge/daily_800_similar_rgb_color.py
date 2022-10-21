class Solution:
    def similarRGB(self, color: str) -> str:

        def find_target(color_section):
            min_diff = float('inf')
            ans = -1

            for i in range(16):
                cur_diff = (int(color_section, 16) - i * 17) ** 2

                if cur_diff < min_diff:
                    min_diff = cur_diff
                    ans = i

            return hex(ans)[-1] * 2

        ans = '#'

        # 1 because given color starts with '#'
        # 1, 3, 5
        for i in range(1, 6, 2):

            # i: 1, 1:3, 3 is exclusive
            ans += find_target(color[i:i + 2])

        return ans
