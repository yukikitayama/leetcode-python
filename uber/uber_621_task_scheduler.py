"""
- If no idle, select a task
- If idle, select a different task
  - if no different task, idle
"""


from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - ord('A')] += 1

        print(f'freqs: {freqs}')

        freqs.sort()
        max_freq = freqs.pop()
        # -1 to find spaces between
        idle_time = (max_freq - 1) * n

        print(f'idle_time: {idle_time}')

        while freqs and idle_time > 0:
            next_max_freq = freqs.pop()

            # When a task with the same freq as the max freq task,
            # n - 1 tasks are filled in idlea spaces, but 1 task is left
            # it will be placed after the max freq task.
            # So for reducing idle time, take min of spaces or number of tasks
            # but later count the task
            idle_time -= min(max_freq - 1, next_max_freq)

        # Turn back the negative to 0
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))




