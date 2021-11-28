class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        tmp = []

        for c in reversed(num):
            if c not in rotated_digits:
                return False
            tmp.append(rotated_digits[c])
        answer = ''.join(tmp)
        return answer == num


num = "69"
# num = "88"
# num = "962"
print(Solution().isStrobogrammatic(num))