class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Edge case: negative
        if x < 0:
            return False

        # Edge case: rightmost digit is 0, but no leading 0
        if x % 10 == 0 and x != 0:
            return False

        reversed_right = 0

        # 1221, terminate: 12 > 12
        # 12021, terminate: 12 > 120
        while x > reversed_right:
            reversed_right = reversed_right * 10 + x % 10
            x //= 10

        print(f"x: {x}, reversed_right: {reversed_right}")

        # second boolean is the odd length case
        return x == reversed_right or x == reversed_right // 10

    def isPalindrome1(self, x: int) -> bool:
        # Edge
        if x < 0:
            return False

        x_str = list(str(x))

        left = 0
        right = len(x_str) - 1

        while left < right:

            if x_str[left] != x_str[right]:
                return False

            left += 1
            right -= 1

        return True
