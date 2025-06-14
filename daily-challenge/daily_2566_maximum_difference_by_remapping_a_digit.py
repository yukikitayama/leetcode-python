class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = str(num)

        i = 0
        while i < len(max_num) and max_num[i] == "9":
            i += 1
        # Here str_num[i] points at 9 or end

        if i < len(max_num):
            # All occurrences are replaced
            max_num = max_num.replace(max_num[i], "9")

        min_num = str(num)
        min_num = min_num.replace(min_num[0], "0")

        return int(max_num) - int(min_num)