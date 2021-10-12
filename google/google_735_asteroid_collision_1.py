from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:

            print(f'new: {new}')

            while ans and new < 0 < ans[-1]:

                if ans[-1] < -new:
                    ans.pop()
                    continue

                elif ans[-1] == -new:
                    ans.pop()

                break

            else:
                ans.append(new)

        return ans


"""
Positive goes right, negative goes left

asteroids = [5,10,-5]
new: 5, while: F, ans: [5]
new: 10, while: T and F = F, ans: [5, 10]
new: -5, while: T and T, if: 10 < 5 = F, elif: 10 == 5 = F, break, 
ans: [5, 10]

asteroids = [8,-8]
new: 8, ans: [8]
new: -8, 

asteroids = [10,2,-5]

asteroids = [1, -2]

asteroids = [-1, -2]

Time complexity
Let n be the length of asteroids. O(n) to iterate each

Space complexity
O(n) for stack?
"""


asteroids = [1, -2]
print(Solution().asteroidCollision(asteroids))

