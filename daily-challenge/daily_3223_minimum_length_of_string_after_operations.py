import collections


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = collections.Counter(s)
        delete_count = 0
        for k, v in counter.items():

            if v % 2 != 0:
                delete_count += v - 1

            elif v % 2 == 0:
                delete_count += v - 2

        return len(s) - delete_count