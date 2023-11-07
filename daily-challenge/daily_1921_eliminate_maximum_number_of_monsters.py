from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrivals = [d / s for d, s in zip(dist, speed)]
        arrivals.sort()

        ans = 0

        for i in range(len(arrivals)):

            # If a monster arrives less than or equal to the weapon time, we lose
            if arrivals[i] <= i:
                break

            # distance >= 1, so arrival > 0, the first monster can be killed
            ans += 1

        return ans



