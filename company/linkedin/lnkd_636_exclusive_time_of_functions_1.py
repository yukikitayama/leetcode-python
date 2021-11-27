"""
- https://leetcode.com/problems/exclusive-time-of-functions/discuss/209173/Python-solution

- list of list [id, start time]
- Initialize ans list size n filled with 0
  - When current process ends,
    - Calculate length
    - Increment ans at the index of the process
- Iterate logs
  - Append log to stack if it's start
  - Pop the top of the stack if the current log is end
    - Calculate time length
    - Increment ans
"""


from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []

        for log in logs:
            id, type, t = log.split(':')
            id = int(id)
            t = int(t)

            print(f'ID: {id}, type: {type}, t: {t}')

            if type == 'start':

                # Stack is nonempty, so we add another function to stack
                # Before that, calculate the exclusive time of the previous function in stack
                # and increment the answer at the previous function index with the amount
                if stack:
                    # current time - start time
                    ans[stack[-1][0]] += t - stack[-1][1]

                stack.append([id, t])

            elif type == 'end':
                prev_id, start_time = stack.pop()

                execution_time = t - start_time + 1

                print(f'    execution_time: {execution_time}')

                ans[id] += execution_time

                # If stack is nonempty
                if stack:
                    # Previous function in the stack resumes at current time + 1
                    # We can update the start time in stack, because the start time before this update
                    # was already used to update the answer in the above 'start if stack: code'
                    stack[-1][1] = t + 1

            print(f'  stack: {stack}')
            print(f'  ans: {ans}')

        return ans


n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(Solution().exclusiveTime(n, logs))

