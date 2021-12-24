class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        str1_to_str2 = {}
        unique_str2_chars = set()

        for char1, char2 in zip(str1, str2):

            if char1 not in str1_to_str2:

                str1_to_str2[char1] = char2
                unique_str2_chars.add(char2)

            elif str1_to_str2[char1] != char2:
                return False

        if len(unique_str2_chars) < 26:
            return True
        else:
            return False
