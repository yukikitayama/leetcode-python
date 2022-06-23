from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        heapq.heapify(heap)
        start = 0
        courses.sort(key=lambda x: x[1])

        for duration, last_day in courses:
            start += duration
            # Max heap to allow us to pop the longest duration class
            heapq.heappush(heap, -duration)

            # If start violates end time, cancel it
            while start > last_day:
                # It uses += so looks like it's incrementing the start time again,
                # but heap actually contains negative numbers, so this successfully
                # decrement start time
                start += heapq.heappop(heap)

        return len(heap)


if __name__ == '__main__':
    # test = [[1, 3], [1, 2], [1, 1]]
    # print(test)
    # test.sort(key=lambda x: (x[0], x[1]))
    # print(test)
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(Solution().scheduleCourse(courses))
