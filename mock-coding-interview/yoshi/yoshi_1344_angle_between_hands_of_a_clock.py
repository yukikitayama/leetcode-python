"""
hour can move 1 / 12 range, 360 / 12 = 30
  15 minute: 30 / 4 = 7.5

Hour movemet
Given minute
  30 * (minute / 60) = 15 deg
  30 * (15 / 60) = 7.5 deg

Get degree between hour and minute
  minute
    0 <= minute <= 60
    * 6
    0 <= degree <= 360

  hour
    0 <= hour <= 12
    * (360 / 12 = 30)
    0 <= degree <= 360

  minute degree - hour degree

  if difference > 180, then return 360 - differece

eg.
  hour = 12, minutes = 30
    minute: 180
    hour: 12 -> 0 -> 0 + (30 * 30 / 60) = 15
    minute - hour = 180 - 15 = 165

"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # Minute to degree
        minute_degree = minutes * 6

        # Hour to degree
        if hour == 12:
            hour = 0
        hour_degree = hour * 30

        # Hour adjustment
        hour_degree += 30 * (minutes / 60)

        print(f"hour_degree: {hour_degree}, minute_degree: {minute_degree}")

        # Compute angle
        angle = abs(minute_degree - hour_degree)

        # Get smaller angle
        if angle > 180:
            angle = 360 - angle

        return angle
