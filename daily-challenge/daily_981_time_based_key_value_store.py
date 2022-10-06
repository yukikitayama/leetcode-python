"""
- heap or binary search
"""


import collections


class TimeMap:
    def __init__(self):
        self.key_time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time_map:
            return ''

        # [0][0] has the earliest timestamp
        if timestamp < self.key_time_map[key][0][0]:
            return ''

        # Binary search
        left = 0
        right = len(self.key_time_map[key])

        while left < right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # Either left - 1 or right - 1 is find
        return self.key_time_map[key][right - 1][1]


class TimeMap1:

    def __init__(self):
        self.key_time_map = collections.defaultdict(collections.defaultdict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time_map:
            return ''

        for curr_time in range(timestamp, 0, -1):
            if curr_time in self.key_time_map[key]:
                return self.key_time_map[key][curr_time]

        return ''


if __name__ == '__main__':
    obj = TimeMap()
    obj.set('foo', 'bar', 1)
    obj.get('foo', 1)
