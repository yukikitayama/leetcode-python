class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            words = [s[i:] + s[:i] for i in range(len(s))]
            return min(words)
        else:
            # List of characters
            chars = sorted(s)
            return ''.join(chars)


if __name__ == '__main__':
    s = 'cba'
    k = 1
    s = 'baaca'
    k = 3
    print(Solution().orderlyQueue(s, k))
