from typing import List
import collections


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_indices = set()

        name_to_data = collections.defaultdict(list)

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")

            name_to_data[name].append((int(time), city, i))

            if int(amount) > 1000:
                invalid_indices.add(i)

        # print(name_to_data)
        # print(invalid_indices)

        for name, data in name_to_data.items():

            # Sort by time, city, index
            data.sort()

            for i in range(len(data)):

                prev = data[i]

                for j in range(i + 1, len(data)):

                    curr = data[j]

                    diff_time = curr[0] - prev[0]

                    if diff_time <= 60:

                        # If different cities
                        if prev[1] != curr[1]:
                            invalid_indices.add(prev[2])
                            invalid_indices.add(curr[2])

                    # If exceed 60 minutes, break to go to the next pair
                    else:
                        break

        # print(invalid_indices)

        return [transactions[i] for i in invalid_indices]

    def invalidTransactions1(self, transactions: List[str]) -> List[str]:
        ans = []

        transactions = [t.split(",") for t in transactions]
        transactions.sort(key=lambda x: (x[0], x[3], x[1]))

        print(transactions)

        prev_name = None
        prev_city = None
        prev_time = None

        for i in range(len(transactions)):

            # $1000
            amount = int(transactions[i][2])
            if amount > 1000:
                ans.append(",".join(transactions[i]))

            # Same name, different city
            else:
                if prev_name is None:
                    prev_name = transactions[i][0]
                    prev_city = transactions[i][3]
                    prev_time = int(transactions[i][1])

                else:
                    curr_name = transactions[i][0]
                    curr_city = transactions[i][3]
                    curr_time = int(transactions[i][1])

                    if prev_name == curr_name and prev_city != curr_city:
                        if prev_time + 60 > curr_time:
                            ans.append(",".join(transactions[i]))
                        else:
                            prev_city = curr_city
                            # [20, 90]
                            prev_time = curr_time
                    else:
                        prev_name = curr_name
                        prev_city = curr_city
                        prev_time = curr_time

        return ans
