from datetime import datetime


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        min_end = min(datetime.strptime(leaveAlice, '%m-%d'), datetime.strptime(leaveBob, '%m-%d'))
        max_start = max(datetime.strptime(arriveAlice, '%m-%d'), datetime.strptime(arriveBob, '%m-%d'))
        delta = (min_end - max_start).days + 1
        return max(0, delta)


if __name__ == '__main__':
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"

    arriveAlice = "10-01"
    leaveAlice = "10-31"
    arriveBob = "11-01"
    leaveBob = "12-31"

    # print(datetime.strptime(leaveAlice, '%m-%d'))
    print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
