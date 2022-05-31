"""
- Make all the binary code patterns
- Bit manipulation?
  - AND operator?
  - In every subset?
- k: 1, {0, 1}, 2, 2^1
- k: 2, {00, 01, 10, 11}, 4, 2^2
- k: 3, {000, 001, 010, 011, 100, ...}, 2^3
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k

        # print(f'need: {need}')

        got = set()

        # e.g. k: 2, i: 2, i - k: 0
        for i in range(k, len(s) + 1):
            sub = s[i - k:i]
            if sub not in got:
                got.add(sub)
                need -= 1
                if need == 0:
                    return True

        return False


if __name__ == '__main__':
    s = "00110110"
    k = 2
    s = "0110"
    k = 2
    print(Solution().hasAllCodes(s, k))
    # print(f'k: {1}, {1 << 1}')
    # print(f'k: {2}, {1 << 2}')
    # print(f'k: {3}, {1 << 3}')
