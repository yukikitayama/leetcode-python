from random import choice


class RandomizedSet:
    def __init__(self):
        # Dictionary with Key: val, Value: index in list
        self.dict = {}
        # List of vals
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If we have the val in our data, return True
        if val in self.dict:
            # Get current data
            last_element = self.list[-1]
            idx = self.dict[val]
            # Update our data by replace the val with the last element
            # So here we have double last elements
            self.list[idx] = last_element
            self.dict[last_element] = idx
            # By delete from the last one, achieve O(1)
            # Remove the val from list
            self.list.pop()
            # Remove the val from dictionary as well
            del self.dict[val]
            return True

        # If we don't have it, return False
        return False

    def getRandom(self) -> int:
        return choice(self.list)


"""
Time complexity
O(1) for getRandom because using random.choice, O(1) for delete because deleting from the last element, 
not by linearly scan a list, O(1) for insert because appending at the end of list and add it to dictionary.

Space complexity
Let n the number of vals to interact. O(n) because O(n) to store array, O(n) to store dictionary, so O(n + n) = O(n)
"""
