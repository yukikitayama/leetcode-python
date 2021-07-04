class Logger:
    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.map:
            self.map[message] = timestamp
            return True

        elif timestamp - self.map[message] >= 10:
            self.map[message] = timestamp
            return True

        else:
            return False
