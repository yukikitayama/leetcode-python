from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0
        ans = 0

        while i < len(chars):

            # Find group length
            group_length = 1
            while i + group_length < len(chars) and chars[i] == chars[i + group_length]:
                group_length += 1

            # Save a group character
            chars[ans] = chars[i]

            # Increment ans because filled the group character
            ans += 1

            # If group length is more than 1, we need to append number
            if group_length > 1:

                str_repr = str(group_length)

                # e.g. "12" -> ["1", "2"]
                chars[ans:ans + len(str_repr)] = list(str_repr)

                ans += len(str_repr)

            # Iterate to the next character group
            i += group_length

        return ans


if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(Solution().compress(chars))
