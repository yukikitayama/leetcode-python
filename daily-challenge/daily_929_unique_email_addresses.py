"""
- Iterate each email in emails
- Iterate each character in each email
  - Skip '.'
  - Encountering '+' or '@' the iteration ends
- Go to the end of email
- Iterate in a reverse order until '@'
- When one email completes, add it to set
- Return the size of the set
"""


from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:

            clean_mail = []

            for curr_char in email:

                if curr_char == '+' or curr_char == '@':
                    break

                if curr_char != '.':
                    clean_mail.append(curr_char)

            domain_name = []
            for curr_char in reversed(email):
                domain_name.append(curr_char)

                if curr_char == '@':
                    break

            clean_mail = ''.join(clean_mail)
            domain_name = ''.join(domain_name[::-1])
            unique_emails.add(clean_mail + domain_name)

        return len(unique_emails)



