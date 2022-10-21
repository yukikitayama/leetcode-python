class Solution:
    def convertToBase7(self, num: int):

        if num == 0:
            return '0'

        elif num < 0:
            tmp = -num
            remainders = []
            while tmp != 0:
                tmp, remainder = divmod(tmp, 7)
                remainders.append(str(remainder))

            ans = int(''.join(remainders[::-1]))
            ans = -ans
            return str(ans)

        else:

            remainders = []

            while num != 0:

                num, remainder = divmod(num, 7)
                remainders.append(str(remainder))

            # print(remainders[::-1])

            return ''.join(remainders[::-1])


if __name__ == '__main__':
    num = 100
    num = 102
    num = -7
    print(Solution().convertToBase7(num))
