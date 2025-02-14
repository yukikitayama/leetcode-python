"""
if store numbers to queue
  add(), T: O(1)
  getProduct() takes T: O(k)

prefix product
nums: [3, 2]
prefix_product: [1, 3, 6]

nums: [3, 2, 0, 2, 3]
prefix_product: [1, 2, 6]
k: 2, 6
k: 3,
"""


class ProductOfNumbers:

    def __init__(self):
        self.array = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.array.append(self.array[-1] * num)
        else:
            self.array = [1]

    def getProduct(self, k: int) -> int:
        if k >= len(self.array):
            return 0
        else:
            return self.array[-1] // self.array[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)