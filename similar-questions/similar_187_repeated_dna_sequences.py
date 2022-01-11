"""
- Similar to 67 Add Binary
"""


from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l, n = 10, len(s)
        if n <= l:
            return []

        # Rolling hash parameters base a
        a = 4
        al = pow(a, l)

        # print(f'a: {a}, al: {al}, 4^10: {4**10}')

        # Convert the given sequence of characters into a list of integers
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        # print(f'nums: {nums}')

        h = 0
        seen, output = set(), set()

        for start in range(n - l + 1):

            if start == 0:
                for i in range(l):
                    h = h * a + nums[i]

            elif start != 0:
                h = h * a - nums[start - 1] * al + nums[start + l - 1]

            if h in seen:
                output.add(s[start:start + l])

            seen.add(h)

        return list(output)


class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 10
        n = len(s)
        seen = set()
        ans = set()

        # O(N - L)
        for i in range(n - l + 1):
            # O(L) to substring
            tmp = s[i:i + l]
            if tmp in seen:
                ans.add(tmp[:])
            seen.add(tmp[:])

        return list(ans)


"""
    - Time is O((N - L) * L)
"""


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
