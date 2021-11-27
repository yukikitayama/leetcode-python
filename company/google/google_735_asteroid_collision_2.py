from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []

        for asteroid in asteroids:
            # Collision happens when right going asteroid is waiting for left going asteroid
            while answer and asteroid < 0 and answer[-1] > 0:

                # Right going asteroid collides with the same size left going asteroid
                if answer[-1] == -asteroid:
                    answer.pop()
                    break

                # Smaller right going asteroid collides with bigger left going asteroid
                elif answer[-1] < -asteroid:
                    answer.pop()
                    # There could be more right going asteroid in answer, so keep while loop until stable
                    continue

                # Bigger right going asteroid collides with smaller left going asteroid
                elif answer[-1] > -asteroid:
                    break

            else:
                answer.append(asteroid)

        return answer


"""
Example
<-, ->
[-1 1]
<-, <-, ->
[-1, -2, 1]

->, <-
[2, -1]
[2] because -1 destroyed by collision

Use another list to observe collision one by one from the lest of the array and store the result
We need to keep observing collision until the asteroids get stable, so use while loop
"""
asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10,2,-5]
# asteroids = [-2,-1,1,2]
print(Solution().asteroidCollision(asteroids))
