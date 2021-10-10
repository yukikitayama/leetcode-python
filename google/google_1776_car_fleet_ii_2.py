from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        # Stack: a list of (position, speend, time to collide with the front car)
        # We need stack because to check the cars in front of the current car
        # As long as there are cars in the stack, we need to check whether the current car will
        # collide all of them
        # Once we know the current car won't collide with the front car, we can remove the front car from stack
        stack = []

        for position, speed in cars[::-1]:

            # print(f'position: {position}, speed: {speed}, stack: {stack}')

            # If the current car speed is faster than the car speed at the stack top, it will collide.
            # Get current car collision time, and get the collision time at the stack top car
            # If current car is slower than the car at the stack top, it won't collide
            # so discard the stack top, because the current top car might be slower
            # by colliding the previous car of the stack top car
            # Remove data from stack 1. if the current car won't collide
            # or 2. if current collision time is later than the front car collision time
            # e.g. for 2, car1 -> car2 -> car3, car2 collides with car3 before car1 collides with car2
            # It will be car1 -> car3 because car2 speed becomes car3 speed
            # So remove car2 from stack and compare car1 and car3
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()

            # The case when there's no front car which the current car will collide
            if not stack:
                stack.append((position, speed, float('inf')))
                result.append(-1.0)

            # The case where the current car will collide
            else:
                collision_time = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collision_time))
                result.append(collision_time)

        # We iterated from the end of the car, so reverse it to be from the start of the car
        result.reverse()

        return result


cars = [[1, 4], [3, 3], [5, 1]]
cars = [[1,2],[2,1],[4,3],[7,2]]
print(Solution().getCollisionTimes(cars))
