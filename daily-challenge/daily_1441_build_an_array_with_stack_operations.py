from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []

        i = 0

        for num in target:

            while i < num - 1:
                ans.append("Push")
                ans.append("Pop")
                i += 1

            ans.append("Push")

            i += 1

        return ans


if __name__ == "__main__":
    print(Solution().buildArray())