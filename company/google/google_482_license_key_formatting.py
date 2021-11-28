class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        # e.g. k: 3, s: aabcabcabc, remainder: 1, and will be a-abc-abc-abc
        # e.g. k: 3, s: abcabcabc, remainder: 0, and will be abc-abc-abc
        remainder = len(s) % k

        # If remainder: 0, the below is ['']
        first_group = [s[0:remainder]]
        # range(start, stop, step), so starts from non-first group and by k length and reach at the end of s
        # k: 4, other_group: ['abcd', 'efgh', ...]
        other_group = [s[i:i+k] for i in range(remainder, len(s), k)]
        # print(other_group)

        if remainder > 0:
            return '-'.join(first_group + other_group)
        else:
            return '-'.join(other_group)


"""
Time complexity
Let n be the length of s
O(n) to format string, O(n / k) to make a other_group list
O(n)

Space complexity
O(n)
"""



# s = "5F3Z-2e-9-w"
# k = 4
s = "2-5g-3-J"
k = 2
print(Solution().licenseKeyFormatting(s, k))
