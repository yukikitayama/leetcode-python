import bisect


class SnapshotArray:
    def __init__(self, length: int):
        self.A = [[[-1, 0]] for _ in range(length)]
        # print(f'self.A: {self.A}')
        # At initialization, we haven't used snap(), so initialize it with 0
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # self.A is a list of lists of lists
        # Self.A[index] is a list of lists that represent vals at index in the array
        # At an index, array stores the data as a list of snapshot ID and the val we set at the ID
        self.A[index].append([self.snap_id, val])
        # print(f'set(index={index}, val={val}): self.A: {self.A}')

    def snap(self) -> int:
        # snap_id is the total number of times to used snap() minus 1
        self.snap_id += 1
        # print(f'snap(): {self.snap_id - 1}')
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # snap_id + 1 because we wanna find the right most index which is between snap_id and snap_id + 1
        # but bisect.bisect() - 1 because actual index is -1 to the above.
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        # print(f'get(index={index}, snap_id={snap_id}): '
        #       f'self.A[index]: {self.A[index]}, '
        #       f'i: {i}')
        # But what we want is not the index in the array. Instead the val we set
        return self.A[index][i][1]


"""
Time complexity
Let s be the number of set called. O(logs) because get() does binary search which is logs

Space complexity
O(s) for self.A
"""


obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
print(f'param_2: {param_2}')
obj.set(0, 6)
param_3 = obj.get(0, 0)
print(f'param_2: {param_3}')