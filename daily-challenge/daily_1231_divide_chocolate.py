"""
- There is n - 1 positions to cut
  - Choose k from n - 1
- Find the maximum possible minimum sum

- Binary search
  - Search the maximum possible minimum total sweetness
  - Search space is min(sweetness) to sum(sweetness) / number of people
  - Find mid num which is not too large and not too small
"""


from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        number_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // number_of_people

        while left < right:

            # left, right, mid are not indices to array in this problem
            # It's the actual number of total sweetness in a piece of chocolate
            mid = (left + right + 1) // 2
            # Total sweetness for the current person
            cur_sweetness = 0
            # The number of people that have a piece of chocolate of sweetness greater than or equal to mid
            people_with_chocolate = 0

            # Start assigning chocolate to the current person
            for s in sweetness:
                cur_sweetness += s

                if cur_sweetness >= mid:
                    people_with_chocolate += 1
                    cur_sweetness = 0

            # Minimum was too small, so raise the minimum
            if people_with_chocolate >= k + 1:
                left = mid
            # Minimum was too large to assign to all people, so decrease maximum
            else:
                right = mid - 1

        return right


sweetness = [1,2,3,4,5,6,7,8,9]
k = 5
sweetness = [5,6,7,8,9,1,2,3,4]
k = 8
sweetness = [1,2,2,1,2,2,1,2,2]
k = 2
print(Solution().maximizeSweetness(sweetness, k))


