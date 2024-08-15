"""
Hashmap
"""

from typing import List
import collections
import math


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        t_count = collections.Counter(target)

        A = []
        for sticker in stickers:
            # Get count value for each letter in sticker
            counter = collections.Counter(sticker)
            # Only keep the key letters which exist in target
            counter &= t_count
            A.append(counter)

        # Remove overlap
        for i in range(len(A) - 1, -1, -1):
            # for j in range(len(A)):
            #     if i != j:
            #         # If A[i] can be found in A[j]
            #         if A[i] & A[j] == A[i]:
            #             A.pop(i)
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        best = len(target) + 1

        def search(res):
            nonlocal best

            if res >= best:
                return

            # If no stickers left and target is satisfied, update answer
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count.keys()):
                    best = res
                return

            # Find maximum number of stickers to use
            sticker = A.pop()
            used = 0
            for letter, count in sticker.items():
                used = max(
                    used,
                    math.ceil(t_count[letter] / count)
                )

            # Reduce the count of target by current sticker
            for letter, count in sticker.items():
                t_count[letter] -= used * count

            # Recursive
            search(res + used)

            # Use less current sticker than max, but explore another sticker
            # Backtrack
            for i in range(used - 1, -1, -1):
                for letter in sticker.keys():
                    t_count[letter] += sticker[letter]
                search(res + i)

            # Backtrack
            A.append(sticker)

        search(0)

        return best if best <= len(target) else -1
