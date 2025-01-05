"""
Simulation
"""

import collections
import heapq


class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {
            "a": "z",
            "b": "y",
            "c": "x",
            "d": "w",
            "e": "v",
            "f": "u",
            "g": "t",
            "h": "s",
            "i": "r",
            "j": "q",
            "k": "p",
            "l": "o",
            "m": "n",
            "n": "m",
            "o": "l",
            "p": "k",
            "q": "j",
            "r": "i",
            "s": "h",
            "t": "g",
            "u": "f",
            "v": "e",
            "w": "d",
            "x": "c",
            "y": "b",
            "z": "a",
        }
        ans = 0
        char_to_max_heap = collections.defaultdict(list)

        for i in range(len(s)):

            if mirror[s[i]] in char_to_max_heap:
                curr_mirror_char = mirror[s[i]]
                buffer = char_to_max_heap[curr_mirror_char]
                # print(buffer)
                j = heapq.heappop(buffer)
                j *= -1
                ans += i - j
                if len(buffer) == 0:
                    del char_to_max_heap[mirror[s[i]]]
                continue

            heapq.heappush(char_to_max_heap[s[i]], -i)

        return ans
