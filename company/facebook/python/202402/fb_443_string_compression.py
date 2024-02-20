"""
insert pointer
  iterate
scan pointer
  counter
  starts from insert pointer position
  while loop
    increment scan pointer
      as long as next is the same character and scan pointer less than length - 1
  insert char
  insert counter depending on the length of string counter
join the chars array from start to the last insert pointer position

"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        scan = 0

        while scan < len(chars):

            counter = 1

            while scan + counter < len(chars) and chars[scan] == chars[scan + counter]:
                counter += 1

            # Insert character
            chars[insert] = chars[scan]
            insert += 1

            # Insert counter if counter is more than 1
            if counter > 1:
                num_digits = len(str(counter))
                chars[insert:insert + num_digits] = list(str(counter))
                # Move insert pointer by the length of digits
                insert += num_digits

            # Go to next scan
            scan += counter

        return insert