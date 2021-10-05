class Logger:
    def __init__(self):
        self.message_to_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_to_timestamp:
            self.message_to_timestamp[message] = timestamp
            return True
        elif message in self.message_to_timestamp:
            recorded_timestamp = self.message_to_timestamp[message]
            if timestamp >= recorded_timestamp + 10:
                self.message_to_timestamp[message] = timestamp
                return True
            else:
                return False


"""
Test
"shouldPrintMessage": [1, "foo"], map: {'foo': 1}, return True
"shouldPrintMessage": [2, "bar"], map: {'foo': 1, 'bar': 2}, return True
"shouldPrintMessage": [3, "foo"], elif: T, recorded_timestamp: 1, if: F, return False
"shouldPrintMessage": [8, "bar"], elif: T, recorded_timestamp: 2, if: F, return False
"shouldPrintMessage": [10, "foo"], elif: T, recorded_timestamp: 1, if: 10 >= 1 + 10 = 10 >= 11 = F, return False
"shouldPrintMessage": [11, "foo"], elif: T, if: 11 >= 11 = T, map: {'foo': 11, 'bar': 2}, return True
"""