"""
Snap
  hashmap
    k: snap_id
    v: array at that time

Ans
  Find highest existing snapshot ID that is less than or equal to a given snapshot ID
"""

import collections


class SnapshotArray:

    def __init__(self, length: int):
        self.index_to_ids_vals = collections.defaultdict(list)
        for i in range(length):
            self.index_to_ids_vals[i].append([0, 0])
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.index_to_ids_vals[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # [[0, 4], [0, 16], [0, 13]]
        # Multiple sets before snap
        # get(0, 0) should get 13
        # Find right insertion point

        ids_vals = self.index_to_ids_vals[index]

        # print(ids_vals)

        left = 0
        right = len(ids_vals) - 1
        while left <= right:
            mid = (left + right) // 2

            if ids_vals[mid][0] == snap_id:
                left = mid + 1

            elif ids_vals[mid][0] < snap_id:
                left = mid + 1

            elif ids_vals[mid][0] > snap_id:
                right = mid - 1

        # print(left, right)

        if left == len(ids_vals):
            return ids_vals[left - 1][1]
        elif ids_vals[left][0] != snap_id:
            return ids_vals[left - 1][1]
        else:
            return ids_vals[left][1]


class SnapshotArray1:

    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_id_to_array = collections.defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snap_id_to_array[self.snap_id] = self.array[:]
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_id_to_array[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)