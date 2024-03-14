"""
hashmap
  k: message
  v: new allowed timestamp

shoudPrintMessage
  if message not in hashmap
    add message with timestamp + 10
    return T
  if message in hashmap
    return F is this timestamp is smaller than hashmap timestamp
    otherwise
      update hashmap with this timestamp + 10 and return T
"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_to_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.message_to_timestamp:
            self.message_to_timestamp[message] = timestamp + 10
            return True

        else:
            if self.message_to_timestamp[message] > timestamp:
                return False
            else:
                self.message_to_timestamp[message] = timestamp + 10
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)