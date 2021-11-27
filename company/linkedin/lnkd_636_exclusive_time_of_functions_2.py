"""
- Initialize ans to an empty list
- Initialize an empty stack []
- iterate logs
  - If it's start,
    - If stack is empty,
      - push the following to stack
        - (function ID, start time)
    - If stack is not empty
      - Get functions ID at the stack top
      - Calculate exclusive time from the start time in stack and the current start time
        - Update ans at index of the stack top function ID
  - If it's end,
    - Calculate exclusive time from the current end time and start time in the stack
    - Pop the item at the top of stack
    - Update stack top functions ID's start time to the current end time
- Return ans
"""


from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []

        for log in logs:

            # print(f'  log: {log}')

            function_id, type, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)

            if type == 'start' and not stack:
                stack.append([function_id, timestamp])

            elif type == 'end':
                start_time = stack[-1][1]
                end_id = stack[-1][0]
                exclusive_time = timestamp - start_time + 1
                ans[end_id] += exclusive_time
                stack.pop()
                if stack:
                    stack[-1][1] = timestamp + 1

            elif type == 'start' and stack:
                start_time = stack[-1][1]
                end_id = stack[-1][0]
                exclusive_time = timestamp - start_time
                ans[end_id] += exclusive_time
                stack.append([function_id, timestamp])

            # print(f'  stack: {stack}')
            # print(f'  ans: {ans}')

        return ans


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(Solution().exclusiveTime(n, logs))







