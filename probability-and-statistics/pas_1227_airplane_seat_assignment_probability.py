"""
- What we want is the probability that person n can get his own seat n
  - Person 1
    - Person 1 takes seat 1
    - Person 1 takes neither seat 1 or seat n
    - These are 1/n + (n - 2)/n
      - n - 2 is n minus seat 1 and seat n
  - Person 2
    - Person 2 takes seat 1
    - Person 2 takes neither seat 1 or seat n
    - These are 1/(n - 1) + (n - 1 - 2)/(n - 1)
      - n - 1 in denominator because person 1 took one of the n seats
      - n - 1 - 2 in numerator because person 1 took one seat and person 2 doesn't select seat 1 and seat n

- I don't know why recursion only multiply (n - 2)/n

Example
- n: 2
  - passenger 1 takes seat 1 or seat 2 with 1/2 probability
  - passenger 2 has seat 2 with the above 1/2 probability

- n: 3
  - passenger 1 takes seat 1, seat 2 or seat 3 with 1/3 probability
    - Probability of seat 3 is not taken is 1 - 2 * 1/3 = 1/3
  - passenger 2 takes the remaining seats with 1/2 probability
    - Probability of seat 3 is not taken is 1/3 * (1 - 1/2) = 1/3 * 1/2 = 1/6
  - passenger 3 takes the remaining last seat

"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 1/n + (n - 2) / n * self.nthPersonGetsNthSeat(n - 1)


print(Solution().nthPersonGetsNthSeat(1))
print(Solution().nthPersonGetsNthSeat(2))
print(Solution().nthPersonGetsNthSeat(3))
