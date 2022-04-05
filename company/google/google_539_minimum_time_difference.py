from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convert(time_str):
            # time_str is 'HH:MM'
            # time_str[:2] is 'HH'
            # time_str[3:] is 'MM'
            return int(time_str[:2]) * 60 + int(time_str[3:])

        minutes = list(map(convert, timePoints))
        minutes.sort()

        # print(minutes)

        ans = float('inf')

        # minutes[1:] + minutes[:1] make it circular to make '23:59' and '00:00' closer
        # for a, b in zip(minutes, minutes[1:] + minutes[:1]):
            # ans = min(ans, (b - a) % (24 * 60))

        # Adding min plus 1440 to minutes to make it circular only for the left and right end
        minutes.append(minutes[0] + 1440)
        for a, b in zip(minutes, minutes[1:]):
            ans = min(ans, b - a)

        return ans


if __name__ == '__main__':
    # timePoints = ["23:59", "00:00"]
    timePoints = ["00:00", "23:59", "00:00"]
    print(Solution().findMinDifference(timePoints))
    # print(23 * 60 + 60)
