from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # By constraints, battery min is 1 and batteries length >= n
        left = 1
        right = sum(batteries) // n
        ans = left

        while left <= right:

            mid = (right + left) // 2

            extra = 0
            for b in batteries:
                # min() because mid is sufficient power that we currently need
                extra += min(b, mid)

            if extra // n >= mid:
                # Save max so far
                ans = mid
                # Explore next search space
                left = mid + 1

            else:
                right = mid - 1

        return ans

    def maxRunTime1(self, n: int, batteries: List[int]) -> int:
        batteries.sort()

        live = batteries[-n:]

        extra = sum(batteries[:-n])

        for i in range(n - 1):

            # Additional power needed to increase running time
            diff = live[i + 1] - live[i]

            # i is 0-based index
            num_computer_add_power = i + 1

            # If we have enough extra power
            if extra // num_computer_add_power >= diff:
                # Reduce extra power to use it
                extra -= diff * num_computer_add_power

            # If it's not sufficient, then stop iteration and return as much as
            # we can additionally supply by remaining extra
            else:
                return live[i] + extra // num_computer_add_power

        # If we still have power, distribute
        return live[-1] + extra // n
