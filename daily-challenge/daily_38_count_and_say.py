class Solution:
    def countAndSay(self, n: int) -> str:

        # Initial value
        current_string = '1'

        # n - 1 because 1 iteration doesn't need to be done because initial value is '1'
        for _ in range(n - 1):

            next_string = ''
            # Inclusive
            left = 0
            # Exclusive
            right = 0
            while left < len(current_string):

                while right < len(current_string) and current_string[right] == current_string[left]:
                    right += 1

                next_string += str(right - left) + current_string[left]

                # Reset for next iteration
                left = right

            # Reset for next iteration
            current_string = next_string

        return current_string


if __name__ == '__main__':
    n = 4
    # 1211
    print(Solution().countAndSay(n))
