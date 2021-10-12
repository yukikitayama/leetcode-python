"""
Idea
- Use answer list as stack


Algorithm
- Iterate each asteroid in asteroids
  - If answer list is empty, append current asteroid to ans
  - If list is not empty, and if the last element is negative, append the current asteroid to ans
    - because [left, right] won't collide
  - if list is not empty, and if the last element is positive, and if the current asteroid is positive,
    append it to ans
  - if list is not empty, if the last element is positive, and if the current asteroid is negative, do collision
    - if last asteroid is bigger than the current negative abs, don't append the current
    - if last asteroid is smaller than the current negative abs, pop the last asteroid from the list,
      append current asteroid
    - if the last asteroid is equal to the current negative abs, pop the last asteroid,
      and don't append current asteroid

We need to do something
- length of ans is bigger than 0 and last asteroid is positive and current asteroid is negative

"""


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:

            while ans and ans[-1] > 0 and asteroid < 0:

                if ans[-1] == abs(asteroid):
                    ans.pop()
                    break

                elif ans[-1] > abs(asteroid):
                    break

                elif ans[-1] < abs(asteroid):
                    ans.pop()

            else:
                ans.append(asteroid)

        return ans


asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10,2,-5]
asteroids = [-2,-1,1,2]
print(Solution().asteroidCollision(asteroids))
