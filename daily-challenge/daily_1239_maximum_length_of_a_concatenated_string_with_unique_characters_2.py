from typing import List
import collections


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def backtracking(pos, res_map):

            # len(res_map) to avoid list index out of range
            # most_common returns a list of tuples. Each tuple contains a character and the count
            # thus most_common(1) returns a length 1 list of a tuple
            # most_common(1)[0]: (ch, count), most_common(1)[0][1]: count
            if len(res_map) and res_map.most_common(1)[0][1] > 1:
                # print(f'res_map.most_common(1): {res_map.most_common(1)}')
                return 0

            ans = len(res_map)

            for i in range(pos, len(arr)):

                # Hashmap with a character as key and count of the character as value
                word_map = collections.Counter(arr[i])

                # word_map is made by arr[i]
                # If their lengths are different, word arr[i] contained duplicated character
                # so cannot proceed
                if len(word_map) != len(arr[i]):
                    # print(f'arr[i]: {arr[i]}, len(word_map): {len(word_map)}, len(arr[i]): {len(arr[i])}')
                    continue

                # res_map has the same structure as word_map
                # counter.update() adds counts
                res_map.update(word_map)

                ans = max(ans, backtracking(i + 1, res_map))

                # Backtrack
                for ch in word_map:
                    if res_map[ch] == word_map[ch]:
                        del res_map[ch]
                    else:
                        res_map[ch] -= word_map[ch]

            return ans

        counter = collections.Counter()
        return backtracking(0, counter)


if __name__ == '__main__':
    arr = ['un', 'iq', 'ue']
    # arr = ['uun', 'iq', 'ue']
    arr = ["cha", "r", "act", "ers"]
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    arr = ["zog","nvwsuikgndmfexxgjtkb","nxko"]
    print(Solution().maxLength(arr))

    # counter = collections.Counter('aabc')
    # print(counter)
    # counter.update('bc')
    # print(counter)
