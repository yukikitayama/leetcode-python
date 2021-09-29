from collections import defaultdict
import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_to_indices = defaultdict(list)
        for index, letter in enumerate(t):
            letter_to_indices[letter].append(index)

        print(f'letter_to_indices:\n{letter_to_indices}')

        curr_match_index = -1

        for letter in s:

            print(f'letter: {letter}')

            if letter not in letter_to_indices:
                return False

            # Lists in each letter is ascending order indices
            # bisect_right, because curr_match_index is current smallest index
            # to get the next index for the same character, need to find right most insertion point
            # match_index is the index to indices in list
            indices_list = letter_to_indices[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)

            print(f'  curr_match_index: {curr_match_index}, match_index: {match_index}')

            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
                print(f'    curr_match_index: {curr_match_index}')
            else:
                return False

        return True


s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
s = "b"
t = "abc"
s = 'abca'
t = 'ahbgdcac'
print(Solution().isSubsequence(s, t))
