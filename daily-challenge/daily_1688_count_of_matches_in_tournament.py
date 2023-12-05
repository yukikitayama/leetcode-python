
class Solution:
    def numberOfMatches(self, n: int) -> int:

        ans = 0

        def recursion(team):

            nonlocal ans

            if team == 1:
                return

            if team % 2 == 0:
                ans += team // 2
                recursion(team // 2)
            else:
                ans += (team - 1) // 2
                recursion((team - 1) // 2 + 1)

        recursion(n)

        return ans


if __name__ == "__main__":
    n = 7
    n = 14
    print(Solution().numberOfMatches(n))
