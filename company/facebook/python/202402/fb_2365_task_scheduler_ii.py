from typing import List


class Solution:
    # def taskSchedulerII(self, tasks: List[int], space: int) -> int:
    # task_to_index = collections.defaultdict(int)

    # ans = 0

    # for i in range(len(tasks)):

    #     task = tasks[i]

    #     if task not in task_to_index:
    #         task_to_index[task] = ans
    #         ans += 1

    #     else:
    #         if ans - task_to_index[task] <= space:

    #             # Can this be math instead of while loop?
    #             while ans - task_to_index[task] <= space:
    #                 ans += 1

    #             task_to_index[task] = ans
    #             ans += 1
    #         else:
    #             task_to_index[task] = ans
    #             ans += 1

    #     # print(i, ans, dict(task_to_index))

    # return ans

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last = {}
        ans = 0

        for i in range(len(tasks)):

            task = tasks[i]

            if task in last:
                ans = max(ans, last[task] + space) + 1
                last[task] = ans

            else:
                ans += 1
                last[task] = ans

            print(i, ans, last)

        return ans
