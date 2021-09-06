class Logger:
    def __init__(self):
        self.message_to_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_to_timestamp:
            self.message_to_timestamp[message] = timestamp
            return True
        elif self.message_to_timestamp[message] + 10 <= timestamp:
            self.message_to_timestamp[message] = timestamp
            return True
        else:
            return False


"""
Time complexity
O(1) because the implementation uses dictionary which allow us to access the data constantly

Space complexity
Let n the number of messages incoming, O(n) to keep dictionary
"""