"""
stream: [3, 0, 2, 5, 4]
prefix product: [3, 1, 2, 10, 40]
- [3, 1, 1*2, 1*2*5, 1*2*5*4]

k: 1, ans: 4, 1*2*5*4 / 1*2*5 = 4
k: 2, ans: 20, 1*2*5*4 / 1*2 = 5*4 = 20
k: 3, ans: 40, 1*2*5*4 / 1 = 2*5*4 = 40
k: 4, ans; 0
"""


class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.prefix_product.append(self.prefix_product[-1] * num)
        else:
            self.prefix_product = [1]

    def getProduct(self, k: int) -> int:

        # Because we always start with extra one length by [1]
        # e.g. first number still product array length is 2,
        # if k == 1, successful
        # but if k == 2, k >= 2 is true, which doesn't exist
        if k >= len(self.prefix_product):
            return 0

        curr_product = self.prefix_product[-1]
        product_excluding_last_k = self.prefix_product[-k - 1]
        return int(curr_product / product_excluding_last_k)


if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
