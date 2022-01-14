"""
- Backtracking
"""


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def valid(segment: str):
            # segment has leading '0', it needs to be '0' only, so len(segment) is 1
            # if segment does not start with '0', the number needs to be less than or equal to 255
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            # n - 1 because index cannot be out of bound of s
            # prev_pos + 4 because 3 positions are enough to contain 255 at max
            # e.g. prev_pos: -1, prev_pos + 4: 3, curr_pos: (0, 1, 2)
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                # e.g. prev_pos: -1, curr_pos: 0, s: '123', s[0:1]: s[0] = '1'
                segment = s[prev_pos + 1: curr_pos + 1]
                if valid(segment):
                    segments.append(segment)
                    # -1 because update_output() makes one more segment
                    if dots - 1 == 0:
                        update_output(curr_pos)
                    else:
                        backtrack(curr_pos, dots - 1)

                    segments.pop()

        n = len(s)
        output, segments = [], []
        backtrack()

        return output


if __name__ == '__main__':
    s = '25525511135'
    print(Solution().restoreIpAddresses(s))
