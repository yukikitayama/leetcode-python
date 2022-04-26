"""
- Convert both to total minutes.
- Try from biggest minute option to decrement
  - and keep track of count of operations
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_minute = 60 * int(current[0:2]) + int(current[3:5])
        correct_minute = 60 * int(correct[0:2]) + int(correct[3:5])

        # Constraints says current <= correct
        diff = correct_minute - current_minute

        # print(f'current_minute: {current_minute}, correct_minute: {correct_minute}, diff: {diff}')

        ans = 0

        for minute in [60, 15, 5, 1]:

            # When minute is bigger than diff,
            # quotient is 0, and diff will be remainder
            quotient, remainder = divmod(diff, minute)

            # print(f'quotient: {quotient}, remainder: {remainder}')

            ans += quotient

            diff = remainder

        return ans


if __name__ == '__main__':
    current = "02:30"
    correct = "04:35"
    print(Solution().convertTime(current, correct))
