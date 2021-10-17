class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_list = s.split()

        # print(f's_list: {s_list}')

        prev = float('-inf')

        for item in s_list:

            if not item.isdigit():
                continue

            elif item.isdigit() and int(item) > prev:
                prev = int(item)

            elif item.isdigit() and int(item) <= prev:
                return False

        return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
s = "hello world 5 x 5"
s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
s = "4 5 11 26"
print(Solution().areNumbersAscending(s))
