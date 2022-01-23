from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        n = len(sample)
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(n + 1 - length):
                num = int(sample[i:i + length])
                if low <= num <= high:
                    ans.append(num)

        return ans


if __name__ == '__main__':
    low = 100
    high = 300
    print(Solution().sequentialDigits(low, high))
