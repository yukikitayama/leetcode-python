"""
- Make a dictionary with key timestamp and value price
- updates(timestamp, value)
  - If the timestamp does not exist in the dictionary keys,
    - Add timestamp as key and value as value
  - If the timestamp exists in the dictionary keys
    - update(timestamp, value) finds the timestamp in keys of the dictionary
      and update the value with value
- maximum()
  - Initialize ans to float('-inf')
  - Iterate key and value in the dictionary
    - ans = max(ans, value)
- minimum()
  - Do the opposite of maximum()
- current()
  - Find the biggest timestamp and return the value
"""


class StockPrice:
    def __init__(self):
        self.timestamp_to_price = {}
        self.latest_timestamp = 0
        self.max_price = 0
        self.min_price = float('inf')

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_to_price[timestamp] = price
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
        if price > self.max_price:
            self.max_price = price
        if price < self.min_price:
            self.min_price = price

    def current(self) -> int:
        # latest_timestamp = 0
        # for timestamp, price in self.timestamp_to_price.items():
        #     if timestamp > latest_timestamp:
        #         latest_timestamp = timestamp
        #         latest_price = price
        # return latest_price

        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self) -> int:
        # max_price = 0
        # for price in self.timestamp_to_price.values():
        #     if price > max_price:
        #         max_price = price
        # return max_price

        return self.max_price

    def minimum(self) -> int:
        # min_price = float('inf')
        # for price in self.timestamp_to_price.values():
        #     if price < min_price:
        #         min_price = price
        # return min_price

        return self.min_price


obj = StockPrice()
obj.update(1, 10)
obj.update(2, 5)
print(obj.current())
print(obj.maximum())
obj.update(1, 3)
print(obj.maximum())
obj.update(4, 2)
print(obj.minimum())

