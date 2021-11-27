from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        # tasks[i]: (start time, processing time, index)
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])

        i = 0
        h = []

        # First start time
        time = tasks[0][0]

        print(f'time: {time}')

        # Finish when all the tasks are appended to answer list
        while len(res) < len(tasks):

            # As long as start time in tasks is earlier than the current time
            # and the index won't be out of boundary
            # tasks[i][0]: start time
            while i < len(tasks) and tasks[i][0] <= time:

                # Push a task to min heap because the start time is earlier than the current time
                # tasks[i][1]: processing time, tasks[i][2]: index
                # priority is the small processing time in priority queue
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))

                print(f'  time: {time}, pushed task: {tasks[i][2]}, '
                      f'the start time: {tasks[i][0]}, process time: {tasks[i][1]}')
                print(f'    heap: {h}')

                # Increment index because we wanna enqueue a task whose start time is the next earliest
                i += 1

                # print(f'    i: {i}')

            # As long as there's a task in priority queue, CPU needs to process it
            if h:
                time_spent_by_task, original_index = heapq.heappop(h)

                # Increase the current time by the time the current task spends
                time += time_spent_by_task

                print(f'    CPU processed task: {original_index}, spent: {time_spent_by_task}, current time: {time}')

                res.append(original_index)

            # Because all the tasks in the priority queue were processed, but there's tasks left
            # So set the current time to the next earliest time
            elif i < len(tasks):
                time = tasks[i][0]

                print(f'      CPU is idle, set current time to {time}')

        return res


tasks = [[1,2],[2,4],[3,2],[4,1]]
tasks = [[1, 2], [5, 1]]
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
tasks = [[1, 1], [1, 1], [1, 1]]
print(Solution().getOrder(tasks))
