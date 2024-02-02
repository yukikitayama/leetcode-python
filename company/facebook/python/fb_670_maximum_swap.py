"""
- Find the max digit and move it to leftmost
- 0 <= num <= 10^8
  - Only from 8 digits to swap 2.
- Kind of backtracking
= 8C2 = 8! / 2! * 6! = 8 * 7 / 2 = 28
"""


# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         # Create a list of integers by making num a string iterable and map each character to integer
#         nums = list(map(int, str(num)))
#
#         print(nums)
#
#         # When duplicate n appear, larger index overwrites smaller
#         num_to_index = {n: i for i, n in enumerate(nums)}
#
#         print(num_to_index)
#
#         for i, n in enumerate(nums):
#
#             for d in range(9, )


# Time: O(N^2) but because of num <= 10^8 constraints, it's okay
class Solution:
    def maximumSwap(self, num: int) -> int:
        tmp = list(str(num))
        # print(tmp)

        # Copy with different reference
        ans = tmp[:]

        for i in range(len(tmp)):
            for j in range(i + 1, len(tmp)):

                # Swap
                tmp[i], tmp[j] = tmp[j], tmp[i]

                if tmp > ans:
                    ans = tmp[:]

                # Backtrack
                tmp[i], tmp[j] = tmp[j], tmp[i]

        return int(''.join(ans))


if __name__ == '__main__':
    num = 2736
    num = 9973
    print(Solution().maximumSwap(num))
