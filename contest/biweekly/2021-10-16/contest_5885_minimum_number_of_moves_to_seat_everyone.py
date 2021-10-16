from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0

        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])

        return ans


seats = [3, 1, 5]
students = [2, 7, 4]
seats = [4,1,5,9]
students = [1,3,2,6]
print(Solution().minMovesToSeat(seats, students))

