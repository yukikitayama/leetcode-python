"""
hashmap
  k: key
  v: list of list: timestamp and value
    [[1, val1], [2, val2], [3, val3]]
      sorted by timestamp,

get
  binary search
    [1]
      1,
      3
    [1, 4]
      4,
      5

[1, 2, 3, 5]
  5: 5
  3: 3
  4: 3
  left insertion point
    mid if target and nums[mid] are the same
    mid - 1 if target and nums[mid] aren't the same

[10, 20]
  t: 5
"""

import collections


class TimeMap:

    def __init__(self):
        self.key_to_value_t_list = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_t_list[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_to_value_t_list:
            return ""

        if timestamp < self.key_to_value_t_list[key][0][0]:
            return ""

        left = 0
        right = len(self.key_to_value_t_list[key]) - 1

        while left <= right:

            mid = (left + right) // 2

            if self.key_to_value_t_list[key][mid][0] == timestamp:
                return self.key_to_value_t_list[key][mid][1]

            elif self.key_to_value_t_list[key][mid][0] < timestamp:
                left = mid + 1

            else:
                right = mid - 1

        # print(f"key: {key}, t: {timestamp}, left: {left}, v_t_list: {self.key_to_value_t_list[key]}")

        if left == len(self.key_to_value_t_list[key]):
            return self.key_to_value_t_list[key][left - 1][1]
        elif self.key_to_value_t_list[key][left][0] > timestamp:
            return self.key_to_value_t_list[key][left - 1][1]
        else:
            return self.key_to_value_t_list[key][left][1]


class TimeMap1:

    def __init__(self):
        self.key_to_value_t_list = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_t_list[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        # if key not in self.key_to_value_t_list:
        #     return ""

        if timestamp < self.key_to_value_t_list[key][0][0]:
            return ""

        v_t_list = self.key_to_value_t_list[key]
        nums = [v_t[0] for v_t in v_t_list]
        index = self.binary_search(nums, timestamp)

        # print(f"key: {key}, t: {timestamp}, index: {index}, v_t_list: {v_t_list}")

        # Given timestamp is largest
        if index == len(nums):
            return v_t_list[-1][1]
        # Prev timestamp is equal to given timestamp
        elif v_t_list[index][0] == timestamp:
            return v_t_list[index][1]
        # Prev timestamp which is smaller than give timestamp doesn't exist
        elif index == 0 and v_t_list[index][0] > timestamp:
            return ""
        # At left insertion point, given timestamp is smaller than prev timestamp
        # so need to get the next smaller prev timestamp
        elif v_t_list[index][0] > timestamp:
            return v_t_list[index - 1][1]

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return left

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)