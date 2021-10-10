"""
distance / time = speed
distance = speed * time
distance / speed = time
"""


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Return the length of the stack as the number of fleets
        stack = []

        for pos, vel in sorted(zip(position, speed))[::-1]:
        # for pos, vel in sorted(zip(position, speed), reverse=True):

            dist = target - pos
            time = dist / vel

            # print(f'pos: {pos}, vel: {vel}, time: {time}')

            if not stack:
                stack.append(time)

            # If the time of the current car is smaller than the time at the top of the stack,
            # then the current car catch up with the car and form a fleet
            # so we don't need to append the current time

            elif time > stack[-1]:
                stack.append(time)

        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(Solution().carFleet(target, position, speed))

