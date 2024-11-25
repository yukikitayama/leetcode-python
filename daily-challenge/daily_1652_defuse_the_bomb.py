from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = [0] * len(code)

        if k == 0:
            return ans

        start = 1
        end = k
        window_sum = 0

        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1

        for i in range(start, end + 1):
            window_sum += code[i]

        for i in range(len(code)):
            ans[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1

        return ans

    def decrypt1(self, code: List[int], k: int) -> List[int]:
        ans = [0] * len(code)

        if k == 0:
            return ans

        for i in range(len(code)):

            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    ans[i] += code[j % len(code)]
            else:
                for j in range(i - 1, i - 1 + k, -1):
                    if j < 0:
                        j += len(code)
                    ans[i] += code[j]

        return ans