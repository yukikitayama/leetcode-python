class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        # 'A' is 65
        # e.g. {'A': 1, 'B': 2, ...}
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}

        # print(alpha_map)

        for i in range(len(columnTitle)):
            curr = columnTitle[len(columnTitle) - i - 1]
            ans += alpha_map[curr] * 26**i

        return ans


if __name__ == '__main__':
    columnTitle = "AB"
    print(Solution().titleToNumber(columnTitle))
