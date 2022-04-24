"""
- {start_station: {end_station: [sum_time, count]}}
- {customer_id: [station_name, t]}
"""


import collections


class UndergroundSystem:
    def __init__(self):
        self.checkin = collections.defaultdict(list)
        self.journey = collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin.pop(id)
        self.journey[(start_station, stationName)][0] += (t - start_time)
        self.journey[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.journey[(startStation, endStation)]
        return total / count


if __name__ == '__main__':
    obj = UndergroundSystem()
    print(obj.checkIn(45, 'Leyton', 3))
    print(obj.checkIn(32, 'Paradise', 8))
    print(obj.checkIn(27, 'Leyton', 10))
    print(obj.checkOut(45, 'Waterloo', 15))
    print(obj.journey)
    print(obj.checkOut(27, 'Waterloo', 20))
    print(obj.checkOut(32, 'Cambridge', 22))
    print(obj.getAverageTime('Paradise', 'Cambridge'))
    print(obj.getAverageTime('Leyton', 'Waterloo'))
