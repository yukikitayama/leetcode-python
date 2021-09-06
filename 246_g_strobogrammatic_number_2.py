class Solution:
    def isStrobogrammatic(self, num: str) -> str:
        rotated_digits = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        left = 0
        right = len(num) - 1

        while left <= right:
            if num[left] not in rotated_digits:
                return False
            if rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


# num = "69"
# num = "88"
num = "962"
print(Solution().isStrobogrammatic(num))
