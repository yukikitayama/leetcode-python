class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:

        if len(password) < 8:
            return False

        lower = upper = digit = special = False

        for i in range(len(password)):

            if i > 0 and password[i] == password[i - 1]:
                return False

            if password[i].islower():
                lower = True

            if password[i].isupper():
                upper = True

            if password[i].isdigit():
                digit = True

            if password[i] in "!@#$%^&*()-+":
                special = True

        if lower and upper and digit and special:
            return True
        else:
            return False