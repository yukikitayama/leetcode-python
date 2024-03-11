"""
h1
  0 if h2 is 0-9
  1 if h2 is 0-9
  2 if h2 is 0-3
h2
  0-9 if h1 is 0 or 1
  0-3 if h1 is 2
m1
  0-5
m2
  0-9

eg1
  2
eg2
  10 * 10 = 100
eg3
  10 * 6 * (10 * 2 + 4 * 1) = 60 * (20 + 4) = 60 * 24 = 1440
"""


class Solution:
    def countTime(self, time: str) -> int:

        ans = 1

        # Hour
        if time[0] == "?" and time[1] == "?":
            ans *= (10 * 2 + 4 * 1)
        elif time[0] == "?" and time[1] != "?":
            if time[1] in ["0", "1", "2", "3"]:
                # 0, 1, 2
                ans *= 3
            else:
                # 0, 1
                ans *= 2
        elif time[0] != "?" and time[1] == "?":
            if time[0] in ["0", "1"]:
                ans *= 10
            elif time[0] in ["2"]:
                # 0, 1, 2, 3
                ans *= 4
        elif time[0] != "?" and time[1] != "?":
            pass

        # Minute
        if time[3] == "?":
            ans *= 6

        if time[4] == "?":
            ans *= 10

        return ans
