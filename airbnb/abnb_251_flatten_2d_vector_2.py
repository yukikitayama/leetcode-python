"""
- Don't rebuild a new data structure from vec in constructor
- next() and hasNext() moves pointers
- At the beginning of next() and hasNext(), call another method to
  move outer index to point at the index which has an integer, or
  move it to the end of vec to say that there's no more integer
"""


from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vector = vec
        self.inner = 0
        self.outer = 0

    def go_to_next_inner_list_if_needed(self):
        # First check self.out index, otherwise the second self.vector[self.outer] throws
        # list index out of range IndexError
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        # Outer index is updated with the below method
        self.go_to_next_inner_list_if_needed()
        result = self.vector[self.outer][self.inner]
        # Inner index is updated with next method
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        # Before this, inner could point at after the end of the inner list
        # With that, we are not sure whether there is the next integer
        # So before this, we use a method to update outer index to move
        # the outer index to the next index at integer or the end of vec to say there's no more integer
        self.go_to_next_inner_list_if_needed()
        return self.outer < len(self.vector)


"""
Complexity
- Time is optimized because constructor does not take O(n)
- next() and hasNext() are O(1) if the helper function does not do its job
  but it will be O(v/n) if the helper function work
- helper function is O(v/n) because
  - it takes O(v + n) in total, but it calls one by one n times in next() and hasNext()
    so the time is amortized by O(v + n) / O(n) = O((v + n) / n)
    = O(v/n + n/n) = (v/n + 1) = O(v/n)
- Space
  - O(1) because vec attribute does not count

Comment
- Optimized solution
"""


vec = [[1, 2], [3], [4]]
obj = Vector2D(vec)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())


