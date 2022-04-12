"""
- Count difference > 1 is impossible
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        count_one = s.count('1')
        count_zero = s.count('0')

        if abs(count_one - count_zero) > 1:
            return -1

        def count_swaps(start):
            count_wrong_position = 0
            for c in s:
                if start != c:
                    count_wrong_position += 1
                # Swap
                start = '1' if start == '0' else '0'
            # when count_zero > count_one, s: 001,
            # count_wrong_position: 2, but swap is only one time, so // 2
            return count_wrong_position // 2

        # When s is odd length, and more 0s, e.g. 010
        # 0 needs to be even index position
        if count_zero > count_one:
            return count_swaps('0')

        # When s is odd length, and more 1s, e.g. 101
        # 1 needs to be even index position
        if count_one > count_zero:
            return count_swaps('1')

        # When s is even length, e.g. 111000, count_swaps('0') returns 2, but count_swaps('1') is 1
        # so min()
        return min(count_swaps('1'), count_swaps('0'))


if __name__ == '__main__':
    s = "111000"
    # e.g. count('0'), 010101, 2 swaps
    # count('1'), 101010, 1 swap
    print(Solution().minSwaps(s))
