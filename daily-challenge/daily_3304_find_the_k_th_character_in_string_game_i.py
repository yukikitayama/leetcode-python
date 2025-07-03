class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ["a"]

        while len(ans) < k:

            curr_len = len(ans)

            for i in range(curr_len):

                c = chr(ord(ans[i]) + 1)
                ans.append(c if c != "z" else "a")

        # print(ans)

        return ans[k - 1]