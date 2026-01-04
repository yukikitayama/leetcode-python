from typing import List
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        div_sum = 0

        for i in nums:
            div_count = 0
            in_sum = 0

            for divisor in range(1, int(math.sqrt(i)) + 1):

                if i % divisor == 0:

                    other = i // divisor

                    if divisor == other:

                        div_count += 1
                        in_sum += divisor

                    else:

                        div_count += 2
                        in_sum += divisor + other

                    if div_count > 4:
                        break

            if div_count == 4:
                div_sum += in_sum

        return div_sum