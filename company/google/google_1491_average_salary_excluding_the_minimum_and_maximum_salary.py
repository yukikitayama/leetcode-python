from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        min_num = float("inf")
        max_num = float("-inf")
        for s in salary:
            min_num = min(min_num, s)
            max_num = max(max_num, s)
            total += s

        return (total - min_num - max_num) / (len(salary) - 2)

    def average1(self, salary: List[int]) -> float:
        min_num = min(salary)
        max_num = max(salary)
        total = 0
        count = 0
        for s in salary:
            if s != min_num and s != max_num:
                total += s
                count += 1
        return total / count