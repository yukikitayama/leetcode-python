class Solution:
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0

        while True:

            buf4 = [""] * 4
            l = read4(buf4)
            self.queue.extend(buf4)

            curr = min(len(self.queue), n - idx)

            for i in range(curr):
                buf[idx] = self.queue.pop(0)
                idx += 1

            if curr == 0:
                break

        return idx
