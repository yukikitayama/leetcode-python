class Solution:
    def __init__(self):
        self.memo = {
            0: 0,
            1: 1
        }

    def fib(self, n: int) -> int:
        if n == 0:
            return self.memo[0]

        elif n == 1:
            return self.memo[1]

        else:
            if n in self.memo:
                return self.memo[n]

            else:
                result = self.fib(n - 1) + self.fib(n - 2)

                self.memo[n] = result

                return self.memo[n]


if __name__ == '__main__':
    n = 2
    # 1
    n = 3
    # 2
    n = 4
    """
    - 3
      - 2
      - 1
    - 2
      - 1
      - 0
      
    """
    print(Solution().fib(n))
