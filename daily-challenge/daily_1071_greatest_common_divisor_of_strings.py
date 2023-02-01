class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)

        def valid(k):

            # If there's remainder, concatenation is impossible
            if m % k or n % k:
                return False

            times_m = m // k
            times_n = n // k

            # Won't be index out of range because taking min
            base = str1[:k]

            return str1 == times_m * base and str2 == times_n * base

        for i in range(min(m, n), 0, -1):

            if valid(i):

                # Won't be index out of range because taking min
                return str1[:i]

        return ""


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1, str2))

