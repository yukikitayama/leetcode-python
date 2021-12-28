from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Key: num in arr, Value: rank
        rank = {}
        # Get a in an ascending order
        for a in sorted(arr):
            # If a exists in rank, return the value
            # If a is not in rank, return len(rank) + 1
            # rank starts from empty dictionary, so it starts with 1
            # e.g. [a, a, b] first a: 1, second a: 1 no change, b: 2 because rank: {'a': 1}
            rank.setdefault(a, len(rank) + 1)
        return list(map(rank.get, arr))

