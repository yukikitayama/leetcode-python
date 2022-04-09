"""
- At second j, jth task is inserted into queue
"""


from typing import List
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []

        # Min heap: [[server weight, server index, current time], ...]
        # smaller weight first, smaller index first
        heap_free_server = [[weight, i, 0] for i, weight in enumerate(servers)]
        heapq.heapify(heap_free_server)

        # Min heap: [[time, server weight, server index], ...]
        heap_running_server = []

        for curr_time, task_time in enumerate(tasks):

            # print(f'curr_time: {curr_time}, task_time: {task_time}')

            # heap_running_server[0][0] is end time
            # When running server end_time <= task_idx (time), this server can be available
            # When server finish running, pop from running heap and add it to free heap
            # When all the servers are running, heap_free_server is empty
            # In that case, pop the smallest end time server from running server heap,
            # and use it as available server. It's fine because below we do max(curr_time, server_time)
            while heap_running_server and heap_running_server[0][0] <= curr_time or not heap_free_server:
            # while heap_running_server and heap_running_server[0][0] <= curr_time:
                end_time, server_weight, server_idx = heapq.heappop(heap_running_server)
                heapq.heappush(heap_free_server, [server_weight, server_idx, end_time])

            # Smallest weight, smallest index server
            weight, server_idx, server_time = heapq.heappop(heap_free_server)

            ans.append(server_idx)

            # max() to update the server time to current time
            end_time = max(curr_time, server_time) + task_time
            heapq.heappush(heap_running_server, [end_time, weight, server_idx])

            # print(f'  running servers: {heap_running_server}')
            # print(f'  available servers: {heap_free_server}')

        return ans


if __name__ == '__main__':
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    # [2, 2, 0, 2, 1, 2]
    servers = [5, 1, 4, 3, 2]
    tasks = [2, 1, 2, 4, 5, 2, 1]
    # [1, 4, 1, 4, 1, 3, 2]
    servers = [10, 63, 95, 16, 85, 57, 83, 95, 6, 29, 71]
    tasks = [70, 31, 83, 15, 32, 67, 98, 65, 56, 48, 38, 90, 5]
    # [8, 0, 3, 9, 5, 1, 10, 6, 4, 2, 7, 9, 0]
    print(Solution().assignTasks(servers, tasks))
