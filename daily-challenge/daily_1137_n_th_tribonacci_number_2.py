class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:

            t_n = 0
            t_n1 = 1
            t_n2 = 1

            for _ in range(n - 2):

                t_n3 = t_n + t_n1 + t_n2

                t_n = t_n1
                t_n1 = t_n2
                t_n2 = t_n3

            return t_n3


if __name__ == "__main__":
    n = 4
    n = 25
    print(Solution().tribonacci(n))

