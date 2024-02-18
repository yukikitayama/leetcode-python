"""
Naive
  class has array
    S: O(N)
  add appends num to array
    T: O(1)
  getProduct gets last k element from array and multiply all
    T: O(N)
    caching

add: 2, add: 2, add: 2
prefix_product: [1, 2, 4, 8]
k: 3 -> prefix_product[-1]
k: 2 -> should be 4, prefix_product[-1] / prefix_product[-3] = 8 / 2 = 4, -3 is -k - 1 = -2 - 1 = -3
  from current prefix product, remove 3rd last prefix product, because we wanna keep last 2 products
  we kept multiplying it, so removing can happening by dividing it
k: 1 -> should be 2, prefix_product[-1] / prefix_product[-2] = 8 / 4 = 2, -2 is -k - 1 = -1 - 1 = -2
  from current prefix product, remove 2nd last prefix product, because we wanna keep last 1 product
"""


class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        # 0 acts as reset
        if num == 0:
            self.prefix_products = [1]
        else:
            prefix_product = self.prefix_products[-1] * num
            self.prefix_products.append(prefix_product)

    def getProduct(self, k: int) -> int:
        # Problem guarantees that we will have k adds before getProduct k
        # But because we reset the array when we got 0,
        # so if k exceeds our array, it means it has 0 sometime before
        if k >= len(self.prefix_products):
            return 0

        else:
            curr_prefix_product = self.prefix_products[-1]
            remove_prefix_product = self.prefix_products[-k - 1]
            return int(curr_prefix_product / remove_prefix_product)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)