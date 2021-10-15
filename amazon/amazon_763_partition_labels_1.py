"""

"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Find the last occurrence of each letter
        # last = {c: i for i, c in enumerate(s)}
        last = {}
        for i, c in enumerate(s):
            # When the same c occurs, overwrite the previous i with the current i
            last[c] = i
            # print(f'  c: {c}, i: {i}')

        print(f'last: {last}')

        # We will have i in the for loop as the end index of the current partition
        # Anchor is the start of the current partition
        # j is the end of the current partition
        # We need to return the size of each partition, so
        # we need j and anchor to have size = i - anchor + 1
        j = anchor = 0

        ans = []

        for i, c in enumerate(s):

            # The maximum index for the characters that have been so far
            j = max(j, last[c])

            # If i is j, current index reached the end index of the current partition
            if i == j:
                ans.append(i - anchor + 1)
                # Because one partition finished,
                # so update the current partition start index anchor to be
                # i: (current end index) + 1
                anchor = i + 1

            print(f'  i: {i}, c: {c}, j: {j}, last[c]: {last[c]}')

        return ans


s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))

