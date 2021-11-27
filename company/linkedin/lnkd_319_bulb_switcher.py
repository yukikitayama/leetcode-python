"""
Example,
- n: 4
  t: 1, [on, on, on, on]
  t: 2, [on, off, on, off]
  t: 3, [on, off, off, off]
  t: 4, [on, off, off, on]
  - 4th round, only toggle 4th bulb

- n: 5
  t: 1, [on, on, on, on, on]
  t: 2, [on, off, on, off, on]
  t: 3, [on, off, off, off, on]
  t: 4, [on, off, off, on, on]
  t: 5, [on, off, off, on, off]
  - 5th round, only toggle 5th bulb

- n: 6
  t: 1, [on, on, on, on, on, on]
  t: 2, [on, off, on, off, on, off]
  t: 3, [on, off, off, off, on, on]
  t: 4, [on, off, off, on, on, on]
  t: 5, [on, off, off, on, off, on]
  t: 6, [on, off, off, on, off, off]

- To get 2 bulbs on, it needs 2^2 = 4 rounds
- To get 3 bulbs on, it needs 3^2 = 9 rounds

- Bulb i is toggled in round t when t divides i
  - e.g. t: 2, 2 divides 4, 4 / 2 = 2
  - so t: 2, every 2nd bulbs are toggled
- All the bulbs start with off,
  - Even number of toggles turn it back to off
  - But odd number of toggles leave the bulbs on
- So if a number if has a odd numbers of divisors,
  the bulb will be toggle odd number of times
- Typical number has even number of divisors
  - e.g. 2 has 1 and 2,
  - e.g., 3 has and 3
  - But squared number of odd number of divisors
    - e.g. 4 has 1, 2, and 4
- So if the bulb number is squared, it will be on at the end
- so out of n bulbs, count the number of squared numbers, including 1
"""


import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))


print(Solution().bulbSwitch(1))
print(Solution().bulbSwitch(2))
print(Solution().bulbSwitch(4))
print(Solution().bulbSwitch(9))
