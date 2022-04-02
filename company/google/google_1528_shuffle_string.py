from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(indices)

        for i, char in enumerate(s):
            ans[indices[i]] = s[i]

        return ''.join(ans)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(Solution().restoreString(s, indices))
