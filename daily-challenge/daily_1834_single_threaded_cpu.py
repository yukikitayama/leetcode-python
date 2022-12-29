from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        ans = []

        sorted_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        sorted_tasks.sort()

        heap = []
        heapq.heapify(heap)

        curr = 0
        task_index = 0

        while task_index < len(tasks) or heap:

            # When idle update current time
            if not heap and curr < sorted_tasks[task_index][0]:
                curr = sorted_tasks[task_index][0]

            while task_index < len(tasks) and curr >= sorted_tasks[task_index][0]:
                _, processing_time, index = sorted_tasks[task_index]
                heapq.heappush(heap, (processing_time, index))
                task_index += 1

            processing_time, index = heapq.heappop(heap)

            curr += processing_time
            ans.append(index)

        return ans


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    # [0,2,3,1]
    # tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    # [4,3,2,0,1]
    print(Solution().getOrder(tasks))
