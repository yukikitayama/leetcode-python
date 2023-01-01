class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        p_to_s = {}
        s_to_p = {}

        for i in range(len(pattern)):

            if pattern[i] not in p_to_s:

                if s_list[i] in s_to_p:
                    return False
                else:
                    p_to_s[pattern[i]] = s_list[i]
                    s_to_p[s_list[i]] = pattern[i]

            else:
                if p_to_s[pattern[i]] != s_list[i]:
                    return False

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"

    pattern = "abba"
    # s = "dog cat cat fish"

    # pattern = "aaaa"
    # s = "dog cat cat dog"

    # pattern = 'abba'
    # s = 'dog dog dog dog'
    print(Solution().wordPattern(pattern, s))

