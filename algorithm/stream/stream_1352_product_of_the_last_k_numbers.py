"""
nums: [2, 5, 4]
prefix_produxt: [2, 10, 40]
k: 1, 40 / 10 = 4
k: 2, 40 / 2 = 20
k: 3, 40 / 1 = 40, if k == len of array, divide by 1
prefix_product[-1] / prefix_product[-(k + 1)]

nums: [2, 5, 4, 8]
prefix_produxt: [2, 10, 40, 320]
k: 2, 320 / 10 = 32

zero
nums: [0, 2, 5, 4]
prefix_product: [0, 2, 10, 40]
if prev is 0, append current num
if divisor is 0, return 0

If we encounter a 0, it nullifies all the products that come after it.
"""


class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
            self.size = 0
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        else:
            return self.prefix_products[-1] // self.prefix_products[-(k + 1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)