class Solution:
    def partitionString(self, s: str) -> int:

        ans = 1

        curr_set = set()

        for ch in s:

            # print(f'ch: {ch}, curr_set: {curr_set}')

            if ch not in curr_set:
                curr_set.add(ch)
            elif ch in curr_set:
                ans += 1
                curr_set = set()
                curr_set.add(ch)

        return ans


if __name__ == '__main__':
    s = "abacaba"
    s = "ssssss"
    print(Solution().partitionString(s))
