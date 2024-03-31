class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Edge
        if num == 1:
            return True

        left = 1
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            squared = mid ** 2

            if squared == num:
                return True

            elif squared > num:
                right = mid - 1

            elif squared < num:
                left = mid + 1

        return False