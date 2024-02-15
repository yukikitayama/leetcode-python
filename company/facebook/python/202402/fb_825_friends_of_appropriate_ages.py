"""
Brute for except themselves
Create function to return boolean by list of conditions with OR, with two ages

T: O(N^2)
  2 * 10^4 * 2 * 10^4

when x < y, no request

If sort in ascending
  No requests from left to right
  Iterate from right
    two pointers
Less than O(N^2), but O(N^2)

example
  x: 30
    2 people
  y: 20
    2 people
  and if condition is valid for x send to y
    each x can send to each y, so 1 * 2 + 1 * 2 = 2 * 2 = 4
"""

from typing import List
import collections


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        def will_send_request(x_age, y_age):
            if (
                    (y_age <= 0.5 * x_age + 7)
                    or (y_age > x_age)
                    or ((y_age > 100) and (x_age < 100))
            ):
                return False

            return True

        # ans = 0

        # for i in range(len(ages)):
        #     for j in range(len(ages)):

        #         if i != j:
        #             x_age = ages[i]
        #             y_age = ages[j]
        #             if will_send_request(x_age, y_age):
        #                 ans += 1

        # return ans

        # ans = 0

        # ages.sort(reverse=True)

        # for left in range(len(ages)):

        #     right = left + 1

        #     while right < len(ages):
        #         x_age = ages[left]
        #         y_age = ages[right]
        #         if will_send_request(x_age, y_age):
        #             ans += 1
        #             if x_age == y_age:
        #                 ans += 1
        #         right += 1

        # return ans

        counter = collections.Counter(ages)
        ans = 0

        # Brute force but key range only from 1 to 120
        for x_age in counter.keys():
            for y_age in counter.keys():

                if x_age != y_age:
                    if will_send_request(x_age, y_age):
                        # Each x person can send to each y person,
                        # so the total number of requests is just the multiplication of 2 counts
                        ans += counter[x_age] * counter[y_age]

                elif x_age == y_age:
                    if will_send_request(x_age, y_age):
                        # -1 removes requests of person A sendiong to person A
                        ans += counter[x_age] * (counter[y_age] - 1)

        return ans
