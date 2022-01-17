"""
- hashmap
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):

            c = pattern[i]
            w = words[i]

            char_key = f'char_{c}'
            word_key = f'word_{w}'

            if char_key not in map_index:
                map_index[char_key] = i

            if word_key not in map_index:
                map_index[word_key] = i

            if map_index[char_key] != map_index[word_key]:
                return False

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    # True
    pattern = "abba"
    s = "dog cat cat fish"
    # False
    print(Solution().wordPattern(pattern, s))
