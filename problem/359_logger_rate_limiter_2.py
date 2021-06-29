class Logger:
    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.map:
            self.map[message] = timestamp
            return True

        elif timestamp >= self.map[message] + 10:
            self.map[message] = timestamp
            return True

        else:
            return False


test = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
logger = Logger()
for timestamp, message in test:
    print(logger.shouldPrintMessage(timestamp, message))
