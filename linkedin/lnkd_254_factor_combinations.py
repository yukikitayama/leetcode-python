"""
- make a list of prime numbers
- backtracking
"""


from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        # n is the current remaining number to be factored
        # i is the current candidate to factor the current remaining number
        # combi is the current sequence of numbers used to factor
        # combis is the answer list
        def factor(n, i, combi, combis):

            # For i to be the number to factor, square of the factor number needs
            # to be smaller than or equal to the remaining number to be factored
            while i * i <= n:

                # For i to be the factor number, remaining of division needs to be 0
                if n % i == 0:

                    # // because inside this if statement it's guaranteed to be divisible
                    # but to avoid the result being float, make the result to be integer
                    combis.append(combi + [i, n // i])

                    print(f'  appended: {combi + [i, n // i]}')

                    factor(n // i, i, combi + [i], combis)

                # Try next candidate factor number
                # it could be prime number, or could be non-prime
                # non-prime will be skipped by the above if n % i == 0
                i += 1

            return combis

        # 2 is the minimum number to be able to factor n
        return factor(n, 2, [], [])


"""
n: 1
factor(1, 2, [], [])
  n: 1, i: 2, combi: [], combis: [],  i * i: 4, while: F, return combis: []
return []

n: 4
factor(4, 2, [], [])
  n: 4, i: 2, combi: [], combis: [], i * i: 4, while: T, n % i: 4 % 2 = 0, if: T,
  combis: [[2, 2]], factor(2, 2, [2], [[2, 2]])
    n: 2, i: 2, combi: [2], combis: [[2, 2]], i * i: 4, while: F, return combis: [[2, 2]]
  i: 3, i * i: 9, while: F, return combis: [[2, 2]]
return [[2, 2]]

n: 8
factor(8, 2, [], [])
  n: 8, i: 2, combi: [], combis: [], i * i: 4, while: T, n % i: 8 % 2 = 0, if: T,
  combis: [[2, 4]], factor(4, 2, [2], [[2, 4]])
    n: 4, i: 2, combi: [2], combis: [[2, 4]], i * i: 4, while: T, n % i: 4 % 2 = 0, if: T,
    combi + [i, n // i]: [2] + [2, 2] = [2, 2, 2], combis: [[2, 4], [2, 2, 2]], factor(2, 2, [2, 2], [[2, 4], [2, 2, 2]])
      n: 2, i: 2, combi: [2], combis: [[2, 4], [2, 2, 2]], i * i: 4, while: F, return combis: [[2, 4], [2, 2, 2]]
    i: 3, i * i: 9, while: F, return combis: [[2, 4], [2, 2, 2]]
  i: 3, i * i: 9, while: F, return combis: [[2, 4], [2, 2, 2]]
return combis: [[2, 4], [2, 2, 2]]
"""


n = 1  # []
n = 12  # [[2,6],[3,4],[2,2,3]]
# n = 37  # []
# n = 32  # [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]
n = 2  # []
n = 3  # []
n = 4  # [[2, 2]]
n = 8
print(Solution().getFactors(n))

