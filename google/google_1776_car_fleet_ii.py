from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        n = len(cars)
        res = []

        # Iterate from the last to the first car
        for position, speed in cars[::-1]:

            # cars[stack[-1]][1]: the speed of the car at the top of the stack.
            # s <= cars[stack[-1]][1]: whether current car is slower than the car in front of the current car
            # cars[stack[-1]][0] - p: distance between current car and the front car
            # If we have [[p1, s1], [p2, s2]], collision time is (p2 - p1) / (s1 - s2), distance / speed
            # (s1 - s2) because s1 is bigger than s2 of front car if s1 car catches up with s2 car
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()

            # If stack is empty, the current car will never collide with the next car
            # because no car is waiting for the current car at the front
            if not stack:
                stack.append((position, speed, float('inf')))
                res.append(-1)

            else:
                collision_time = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collision_time))
                res.append(collision_time)

        res.reverse()

        return res


"""
time = distance / speed
"""
