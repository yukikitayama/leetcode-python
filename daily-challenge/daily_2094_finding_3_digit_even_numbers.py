from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if num >= 100 and num % 2 == 0:
                        ans.add(num)

        return sorted(list(ans))