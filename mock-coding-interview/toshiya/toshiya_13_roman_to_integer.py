class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        ans = 0
        i = 0
        while i < len(s):

            if i < len(s) - 1 and s[i:i + 2] in roman_to_int:
                ans += roman_to_int[s[i:i + 2]]
                i += 2

            else:
                ans += roman_to_int[s[i]]
                i += 1

        return ans

    def romanToInt1(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        i = 0

        ans = 0

        while i < len(s):

            if (
                    (s[i] == "I" and i < len(s) - 1 and s[i + 1] in ["V", "X"])
                    or (s[i] == "X" and i < len(s) - 1 and s[i + 1] in ["L", "C"])
                    or (s[i] == "C" and i < len(s) - 1 and s[i + 1] in ["D", "M"])
            ):
                num = roman_to_int[s[i: i + 2]]
                i += 2
            else:
                num = roman_to_int[s[i]]
                i += 1

            ans += num

            print(num)

        return ans
