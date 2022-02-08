class Solution:
    def addDigits(self, num: int) -> int:
        # ans = num
        # while len(str(ans)) > 1:
        #     ans = sum([int(v) for v in str(ans)])
        # return ans
        if num == 0:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    num = 38
    print(Solution().addDigits(num))
