from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # results will contains all the combination
        results = [""]
        best = 0

        for word in arr:

            # print(f'word: {word}')

            for i in range(len(results)):

                new_res = results[i] + word

                # print(f'results[i]: {results[i]}, new_res: {new_res}')

                # Check if the concatenation of a subsequence of arr has unique characters
                # If not unique, we can't add them to answer candidate, so continue to skip
                if len(new_res) != len(set(new_res)):
                    continue

                results.append(new_res)

                best = max(best, len(new_res))

        return best


arr = ["un","iq","ue"]
print(Solution().maxLength(arr))

