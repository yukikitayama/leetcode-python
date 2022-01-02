from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recursion(start, end, ls):
            if start >= end:

                # print(ls)

                # None because this problem doesn't require to return anything
                # but it needs to stop the recursion
                return None

            ls[start], ls[end] = ls[end], ls[start]

            return recursion(start + 1, end - 1, ls)

        return recursion(0, len(s) - 1, s)


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s))
