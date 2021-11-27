"""
- Initlialize counter to 0
- Use a for loop to generate integer from 1
  - if the generated integer is the integer whose prime factors are limited to 2, 3, 5, then increment counter
  - if counter == n, break the for loop
- return the last generated integer

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:

            # If the last num in ugly is greater than or equal to the previous (2, 3, 5) prime factor number,
            # we increment the index for (2, 3, 5), because we need to append them to ugly
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1

            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1

            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1

            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))

        return ugly[-1]

"""
ugly: [1], i2: 0, i3: 0, i5: 0
while1: T, while2: F, while3: F, while4: F, ugly: [1, 2]
len(ugly): 2, while1: T, ugly[i2] * 2: 2, ugly[-1]: 2, while2: T, i2: 1, ugly[i2] * 2: 4, ugly[-1]: 2, while2: F,
ugly[i3] * 3: 3, ugly[-1]: 2, while3: F, while4: F, ugly: [1, 2, 3], 
len(ugly): 3, while1: T, while2: F, ugly[i3] * 3: 3, ugly[-1]: 3, while3: T, i3: 1,
"""

