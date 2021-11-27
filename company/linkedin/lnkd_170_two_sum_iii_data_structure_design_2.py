import collections


class TwoSum:
    def __init__(self):
        self.num_to_count = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.num_to_count[number] += 1

    def find(self, value: int) -> bool:
        for num in self.num_to_count:
            complement = value - num
            if complement != num and complement in self.num_to_count:
                return True
            elif complement == num and self.num_to_count[num] > 1:
                return True
        return False


"""
Complexity
- Time
  - Constructor O(1)
  - add O(1)
  - find O(n) by removing nlogn sort
- Space
  - O(n) for hashmap
"""


obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))