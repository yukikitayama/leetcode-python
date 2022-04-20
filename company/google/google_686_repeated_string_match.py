class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        tmp = ''
        count = 0

        # Terminate when current string is longer than the length of sum of a and b
        # It means that even if we add any more a to current string, the result won't change
        # b just doesn't exist as substring in the current string
        # so out of this while loop, just return -1
        while len(tmp) < len(b) + len(a):
            tmp += a
            count += 1

            # Check if b is substring of repeated a
            if b in tmp:
                return count

        return -1


if __name__ == '__main__':
    a = "abcd"
    b = "cdabcdab"
    print(Solution().repeatedStringMatch(a, b))
