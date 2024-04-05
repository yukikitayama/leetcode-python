class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_divisible(k):
            if len1 % k != 0 or len2 % k != 0:
                return False

            count1 = len1 // k
            count2 = len2 // k

            candidate = str1[:k]

            return str1 == candidate * count1 and str2 == candidate * count2

        for i in range(min(len1, len2), 0, -1):
            if is_divisible(i):
                return str1[:i]
        return ""

    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            candidate = str1
            bigger = str2
        else:
            candidate = str2
            bigger = str1

        # print(candidate)

        candidates = []
        for i in range(len(candidate)):
            for j in range(i + 1, len(candidate) + 1):
                sub = candidate[i:j]
                candidates.append(sub)
        candidates = list(set(candidates))
        candidates.sort(key=lambda x: len(x), reverse=True)

        # print(candidates)

        def is_divisible(str_, divisor):
            left = 0

            while left < len(str_):

                if str_[left:left + len(divisor)] == divisor:
                    left += len(divisor)
                else:
                    break

            if left == len(str_):
                return True
            else:
                return False

        for candidate in candidates:

            if is_divisible(str1, candidate) and is_divisible(str2, candidate):
                return candidate

            else:
                continue

        return ""
