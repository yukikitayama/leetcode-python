"""
A -> 1
Z -> 26

AA -> 27 = 1 + 26
AB -> 28 = 2 + 26
AZ -> 58 = 26 + 26

BA -> 59 = 2 * 26 + 1
BZ -> 2 * 26 + 26

ZA -> 26 * 26 + 1
ZZ -> 26 * 26 + 26

AAA -> 59 = (1 * 26**2) + (1 * 26) + 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

        # print(capitals)

        ans = []

        # Getting character in reverse order
        # reverse because of modulo
        while columnNumber > 0:

            # -1 because 0-based index
            remain = (columnNumber - 1) % 26
            ans.append(capitals[remain])

            columnNumber = (columnNumber - 1) // 26

        return ''.join(ans[::-1])


if __name__ == '__main__':
    columnNumber = 1 * 26**2 + 1 * 26 + 26
    print(Solution().convertToTitle(columnNumber))
