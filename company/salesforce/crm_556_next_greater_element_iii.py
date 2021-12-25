"""
n: 13
ans: 31
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = [char for char in str(n)]

        # print(f'a: {a}')

        # -2 to avoid index out of bound and i+1 pointer
        i = len(a) - 2

        # As long as descending order
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1

        # If the above loop led us to the beginning, no way to find the next greater integer
        if i < 0:
            return -1

        j = len(a) - 1
        # Find the next grater element (a[j]) than a[i]
        # j is to the right of i
        while j >= 0 and a[i] >= a[j]:
            j -= 1

        # Swap
        a[i], a[j] = a[j], a[i]

        # Reverse
        start = i + 1
        end = len(a) - 1
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1

        # print(f'a: {a}')

        ans = int(''.join(a))

        # print(f'ans: {ans}, type: {type(ans)}')

        if ans > 2**31 - 1:
            return -1
        else:
            return ans


n = 12
# n = 13
# n = 21
# n = 2147483486  # -1
print(Solution().nextGreaterElement(n))

