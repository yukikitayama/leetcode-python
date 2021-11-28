from collections import defaultdict
import bisect


class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        # print(f'source: {source}, target: {target}')

        # Key: character in source, value: list of indices of the character in source
        inverted_index = defaultdict(list)
        for i, ch in enumerate(source):
            inverted_index[ch].append(i)

        # print(f'inverted_index: {inverted_index}')

        # Why initialized with 1
        loop_cnt = 1

        # i is the index to be inserted to the list in inverted_index dictionary
        i = -1
        for ch in target:

            # print(f'ch: {ch}, i: {i}, loop_cnt: {loop_cnt}')

            if ch not in inverted_index:
                return -1

            offset_list_for_ch = inverted_index[ch]

            # print(f'offset_list_for_ch: {offset_list_for_ch}')

            j = bisect.bisect_left(offset_list_for_ch, i)

            # print(f'bisect_left({offset_list_for_ch}, i={i}): j={j}')

            # print(f'j: {j}, i: {i}')

            # When j is equal to length of inverted index list,
            # the current character from target gets outside of the character index list from source
            # So it needs to go back to the end to get a smaller index, and plus one for the next character
            # , so increment loop_cnt
            if j == len(offset_list_for_ch):
                loop_cnt += 1
                # [0]? => current character from target gets out of the list from source, so go back to the beginning
                # and plus one for the next character
                i = offset_list_for_ch[0] + 1
            else:
                # + 1 for the next character
                i = offset_list_for_ch[j] + 1

            # print()

        return loop_cnt



source = "abc"
target = "abcbc"
# 2
source = "abc"
target = "acdbc"
# -1
source = "xyz"
target = "xzyxz"
# 3
source = "abcab"
target = "aabbaac"
# 3
print(Solution().shortestWay(source, target))

