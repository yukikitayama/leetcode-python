from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        ans = 0

        for chars in zip(*strs):

            for i, ch in enumerate(chars):
                if i == 0:
                    curr = ord(ch)

                elif curr <= ord(ch):
                    curr = ord(ch)

                else:
                    ans += 1
                    break

        return ans


if __name__ == '__main__':
    strs = [
        "cba",
        "daf",
        "ghi"
    ]
    # 1
    strs = ["a", "b"]
    # 0
    strs = ["zyx", "wvu", "tsr"]
    # 3
    print(Solution().minDeletionSize(strs))

