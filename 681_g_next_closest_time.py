class Solution:
    def nextClosestTime(self, time: str) -> str:
        # String time expression to minute integer
        current_total_minute = 60 * int(time[:2]) + int(time[3:])
        # Make a set containing each digit in time string
        allowed = {int(x) for x in time if x != ':'}
        # print(f'type(allowed): {type(allowed)} allowed: {allowed}')

        while True:
            # Keep incrementing the time by one minute until we get the desired value
            # 23:59 => 1439 => 1439 % (24 * 60) => 1439 % 1440 => 1439
            # 24:00 or 00:00 both produce 0 by % (24 * 60)
            current_total_minute = (current_total_minute + 1) % (24 * 60)

            # will be 1 if a new digit is not in allowed
            flag = 0

            # divmod() returns quotient and remainder.
            # so the below first iteration is block: quotient, second iteration is block: remainder
            # The below convert minute in total to hour: quotient, minute: remainder
            # e.g. 19:35 => (19 * 60) + 35 => 1175 minutes => divmod(1175, 60) => (19, 35)
            for hour_and_minute in divmod(current_total_minute, 60):

                # The below converts 2 digits hour and minute to 1 digits
                # e.g. 19 hour => (1, 9), 35 minute => (3, 5)
                for digit in divmod(hour_and_minute, 10):

                    # Need to reuse the current digits, so if we got a digit not in the current digit
                    # It's not the digit we return
                    if digit not in allowed:
                        flag = 1

                if flag:
                    # break the outer for loop. Not break for while loop
                    # So go to the next combination of hour and minute
                    break

            if not flag:
                hour, minute = divmod(current_total_minute, 60)
                hour = '0' + str(hour) if hour < 10 else str(hour)
                minute = '0' + str(minute) if minute < 10 else str(minute)
                return hour + ':' + minute


"""
Time complexity
Even if it uses while loop and nested for loop, time is bounded, because we are guaranteed to get a new time
so O(i)

Space complexity
O(1) because we only need length 4 set and temporary variables
"""


time = '19:34'
time = '20:48'
print(Solution().nextClosestTime(time))

cur = 60 * int(time[:2]) + int(time[3:])
print(f'cur: {cur}')
cur = (cur + 1) % (24 * 60)
print(f'cur: {cur}')
for block in divmod(cur, 60):
    print(f'block: {block}')

