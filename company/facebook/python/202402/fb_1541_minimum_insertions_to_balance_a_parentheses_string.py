"""
opening as +1
closing as -0.5

counter starts with 0

count open and close separately
compute balance by open - close
when close is -2
  count up ans by 1
  reset close to 0
when balance is 0
  decrement open counter by 1
  decrement close counter by 2
"""


class Solution:
    def minInsertions(self, s: str) -> int:

        insert_count = 0
        balance = 0

        i = 0

        while i < len(s):

            ch = s[i]

            if ch == ")":

                # If we have 2 closes
                if i < len(s) - 1 and s[i + 1] == ")":

                    # If we had open previously and can clear balance
                    if balance > 0:
                        balance -= 1

                    # Id we didn't have open previously, we need to add 1 open
                    else:
                        insert_count += 1

                    # At the bottom i moves by 1, but in this if block, we need to skip the next close
                    i += 1

                # If we had open, but because next is not another close, so we cannot close, but we wanna close
                elif balance > 0:
                    # We need to insert one close
                    insert_count += 1
                    # Then we can clear one balance
                    balance -= 1

                # Otherwise, we need to insert one open and open close
                # We dont' need to touch balance, because there was not open before
                else:
                    insert_count += 2

            elif ch == "(":
                balance += 1

            i += 1

        # When we have positive balance, it's the number of open
        # But we need to have twice close of it to close
        # And of course insert_count needs to be included to get total number of insertions
        return balance * 2 + insert_count
