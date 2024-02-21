"""
n depends on the output of n - 1, so need recursion

n: 5
  1211, 111221
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        def recursion(num):

            if num == 1:
                return "1"

            res = recursion(num - 1)

            # 1
            # 1211 -> 111221
            ans = []
            i = 0
            while i < len(res):

                count = 1

                while i < len(res) - 1 and res[i] == res[i + 1]:
                    i += 1
                    count += 1

                ans.append(str(count) + res[i])
                i += 1

            # print(num, ans)

            return "".join(ans)

        return recursion(n)


