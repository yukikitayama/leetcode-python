class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)

        # Mid
        if len_n % 2 == 0:
            # -1 for 0-based index
            i = len_n // 2 - 1
        else:
            i = len_n // 2

        def half_to_palindrome(left, even):
            # print(f"  left: {left}, even: {even}")

            res = left

            # If odd, mid number is contained in left, so remove the right most number
            if not even:
                left = left // 10

            while left > 0:
                # Get right most digit of left half
                # and append it to the right most of left half
                # e.g. left: 123, res: 123,
                # before iter, left: 12, res: 123
                # after 1st iter, res: 1232, res: 12
                # after 2nd iter, res: 12321, res: 1
                res = res * 10 + left % 10
                left //= 10

            # print(f"  res: {res}")

            return res

        possibilities = []

        # n: 12345, i: 2, first_half: 123
        # n: 1234, i: 1, first_half: 12
        first_half = int(n[:i + 1])

        # print(f"i: {i}, first_half: {first_half}")

        # Generate all the palindrome which are near
        possibilities.append(half_to_palindrome(first_half, len_n % 2 == 0))
        # Because keeping palindrome, only increment or decrement middle number
        possibilities.append(half_to_palindrome(first_half + 1, len_n % 2 == 0))
        possibilities.append(half_to_palindrome(first_half - 1, len_n % 2 == 0))
        # Edge case
        remove_digit = 10 ** (len_n - 1) - 1
        # print(f"remove_digit: {remove_digit}")
        possibilities.append(remove_digit)
        add_digit = 10 ** len_n + 1
        # print(f"add_digit: {add_digit}")
        possibilities.append(add_digit)

        ans = 0
        min_diff_so_far = float("inf")
        int_n = int(n)

        for candidate in possibilities:

            if candidate == int_n:
                continue

            if abs(candidate - int_n) < min_diff_so_far:
                min_diff_so_far = abs(candidate - int_n)
                ans = candidate

            # Edge case
            elif abs(candidate - int_n) == min_diff_so_far:
                ans = min(ans, candidate)

        return str(ans)