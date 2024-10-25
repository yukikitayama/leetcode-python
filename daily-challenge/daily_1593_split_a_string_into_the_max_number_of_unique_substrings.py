class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def backtracking(index):

            if index == len(s):
                return 0

            res = 0

            for i in range(index + 1, len(s) + 1):

                sub_str = s[index:i]

                if sub_str not in seen:
                    seen.add(sub_str)
                    res = max(res, 1 + backtracking(i))
                    seen.discard(sub_str)

            return res

        return backtracking(0)