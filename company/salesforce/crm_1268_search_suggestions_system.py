from typing import List
import bisect


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        ans = []
        prefix = ""
        i = 0

        for ch in searchWord:

            prefix += ch

            i = bisect.bisect_left(products, prefix, lo=i)

            curr = []
            for product in products[i: i + 3]:
                if product.startswith(prefix):
                    curr.append(product)

            ans.append(curr)

        return ans
