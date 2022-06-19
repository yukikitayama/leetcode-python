"""
- Trie
- Lexicographically sorted at most 3 words

- Binary search the position of prefix, and check if the next 3 words are valid
"""


from typing import List
import bisect


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        ans = []
        prefix = ''
        i = 0

        for c in searchWord:
            # In each type, prefix gets longer
            prefix += c

            # Find the index of prefix match
            i = bisect.bisect_left(products, prefix, lo=i)

            curr = []
            # [i:i + 3] because at most 3 words
            for product in products[i:i + 3]:
                if product.startswith(prefix):
                    curr.append(product)

            ans.append(curr)

        return ans


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(Solution().suggestedProducts(products, searchWord))
