"""
Merge requirements
  Share the same email

hashmap
  k: name
    Differentiate different people with the same name
  v: set of emails

Convert array of email addresses into set
If there are intersection of two sets, merge the account
  Union is the email list after merging

Same name, no intersection
  hashmap
    k: name
    v: list of set

At the end
  When creating the answer list from hashmap and hashset, sort the list

Edge
  Different name, but share the same email

eg
[
    ["David","David0@m.co","David1@m.co"],  a -> b
    ["David","David3@m.co","David4@m.co"],  b
    ["David","David4@m.co","David5@m.co"],  b
    ["David","David2@m.co","David3@m.co"],  b
    ["David","David1@m.co","David2@m.co"]
    ]


"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjacent = collections.defaultdict(list)

        def dfs(merged_account, email):
            visited.add(email)
            merged_account.append(email)

            # If account has only one email, it's not included in adjacent
            if email not in adjacent:
                return

            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(merged_account, neighbor)

        account_list_size = len(accounts)

        # Create graph
        for account in accounts:

            account_size = len(account)

            account_first_email = account[1]

            # 2 is second email
            for j in range(2, account_size):
                account_email = account[j]

                adjacent[account_first_email].append(account_email)
                adjacent[account_email].append(account_first_email)

        # When account has only one email, adjacent doesn't contain it
        print(adjacent)

        # Traverse
        ans = []

        for account in accounts:

            account_name = account[0]
            account_first_email = account[1]

            if account_first_email not in visited:
                merged_account = [account_name]

                dfs(merged_account, account_first_email)

                emails = merged_account[1:]
                emails.sort()
                merged_account[1:] = emails
                ans.append(merged_account)

        return ans

    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

    #     name_to_address = collections.defaultdict(list)

    #     for i in range(len(accounts)):

    #         account = accounts[i]
    #         name = account[0]
    #         emails = set(account[1:])

    #         if name not in name_to_address:
    #             name_to_address[name].append(emails)

    #         else:
    #             list_of_set = name_to_address[name]
    #             found = False

    #             for i in range(len(list_of_set)):

    #                 email_set = list_of_set[i]

    #                 # Common account
    #                 if len(emails.intersection(email_set)) > 0:
    #                     list_of_set[i] = emails.union(email_set)
    #                     found = True

    #             # If common account not found, need to add new
    #             if not found:
    #                 name_to_address[name].append(emails)

    #     # Final adjustment

    #     print(name_to_address)

    #     # {name1: [{}, {}], name2: [{}]}
    #     ans = []
    #     for k, v in name_to_address.items():
    #         for email_set in v:
    #             account = [k]
    #             account.extend(sorted(list(email_set)))
    #             ans.append(account)

    #     return ans