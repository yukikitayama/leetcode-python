class TwoSum:
    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:

        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        left = 0
        right = len(self.nums) - 1

        while left < right:

            curr_sum = self.nums[left] + self.nums[right]

            if curr_sum == value:
                return True
            elif curr_sum < value:
                left += 1
            else:
                right -= 1

        return False


"""
Complexity
- Time
  - Constructor O(1)
  - add O(1)
  - find, sort takes O(nlogn) and while loop takes O(n), so O(nlogn)
- Space
  - O(n) for list
"""


obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))