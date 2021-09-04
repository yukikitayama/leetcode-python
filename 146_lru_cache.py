from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.ordered_dict:
            return -1

        self.ordered_dict.move_to_end(key)
        return self.ordered_dict[key]

    def put(self, key: int, value: int) -> None:
        # If key exists, move to end as recently used
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        # Update value
        self.ordered_dict[key] = value

        # If cache is over capacity, remove the least recently used item
        # which is at the beginning of the ordered dictionary
        if len(self.ordered_dict) > self.capacity:
            # last=True pops the recently used item, so last=False to remove the beginning item
            self.ordered_dict.popitem(last=False)

