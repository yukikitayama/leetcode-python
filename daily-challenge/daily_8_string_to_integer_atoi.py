class StateMachine:
    def __init__(self):
        self.State = {'q0': 1, 'q1': 2, 'q2': 3, 'qd': 4}
        self.INT_MAX = pow(2, 31) - 1
        self.INT_MIN = -pow(2, 31)
        # Super private variable accessible by
        self.__current_state = self.State['q0']
        self.__result = 0
        self.__sign = 1

    def to_state_q1(self, ch: chr) -> None:
        self.__sign = -1 if (ch == '-') else 1
        self.__current_state = self.State['q1']

    def to_state_q2(self, digit: int) -> None:
        self.__current_state = self.State['q2']
        self.append_digit(digit)

    def to_state_qd(self) -> None:
        self.__current_state = self.State['qd']

    def append_digit(self, digit: int) -> None:
        if (self.__result > self.INT_MAX // 10) or (self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10):
            if self.__sign == 1:
                self.__result = self.INT_MAX
            else:
                self.__result = self.INT_MIN
                self.__sign = 1
            self.to_state_qd()
        else:
            self.__result = (self.__result * 10) + digit

    def transition(self, ch: chr) -> None:
        if self.__current_state == self.State['q0']:
            if ch == ' ':
                # Stay in the same state
                return
            elif ch == '-' or ch == '+':
                self.to_state_q1(ch)
            elif ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

        elif self.__current_state == self.State['q1'] or self.__current_state == self.State['q2']:
            if ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

    def get_integer(self) -> int:
        return self.__sign * self.__result

    def get_state(self) -> int:
        return self.__current_state


class Solution:
    def myAtoi(self, s: str) -> int:
        q = StateMachine()

        for ch in s:
            q.transition(ch)
            if q.get_state() == q.State['qd']:
                break

        return q.get_integer()


class Solution1:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Ignore leading spaces
        while index < n and s[index] == ' ':
            index += 1

        # Check sign
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1

        # Traverse digits and stop if it's not a digit
        while index < n and s[index].isdigit():

            digit = int(s[index])

            # Check overflow and underflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1

        return sign * result


if __name__ == '__main__':
    s = '42'
    s = "   -42"
    s = "4193 with words"
    print(Solution().myAtoi(s))
