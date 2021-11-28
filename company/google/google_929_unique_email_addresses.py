from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for email in emails:

            # Clean email is a list of characters
            clean_email = []

            # Iteration for local name
            for char in email:

                if char == '+' or char == '@':
                    break

                if char != '.':
                    clean_email.append(char)

            # Iteration for domain name
            domain_name = []
            for char in reversed(email):
                domain_name.append(char)
                if char == '@':
                    break

            # From lists of characters to string
            domain_name = ''.join(domain_name[::-1])
            clean_email = ''.join(clean_email)
            email_set.add(clean_email + domain_name)

        return len(email_set)


"""
Time complexity
Let n be the number of emails, m be the average length of emails
O(nm) because algorithm iterates each email and each character of the email

Space complexity
In the worst case, all the emails are unique, so the size of set is n * m, O(nm)
"""


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))
