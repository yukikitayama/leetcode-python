"""
Simulation
  Make both arrays queue
    students queue
      [(student preference, seen boolean)]
        if seen and current sandwitch isn't preference
          break
"""

from typing import List
import collections


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = collections.Counter(students)
        num_aet = 0
        for i in range(len(sandwiches)):

            if counter[sandwiches[i]] == 0:
                break

            else:
                counter[sandwiches[i]] -= 1
                num_aet += 1

        return len(students) - num_aet

    def countStudents2(self, students: List[int], sandwiches: List[int]) -> int:
        ans = 0
        sandwich_stack = [s for s in sandwiches[::-1]]
        student_queue = collections.deque(students)
        unserved = 0

        while True:

            student_pref = student_queue.popleft()

            if student_pref == sandwich_stack[-1]:
                sandwich_stack.pop()
                unserved = 0

            else:
                unserved += 1
                student_queue.append(student_pref)

            if unserved == len(student_queue):
                break

        return len(sandwich_stack)

    def countStudents1(self, students: List[int], sandwiches: List[int]) -> int:
        ans = 0

        sandwich_queue = collections.deque(sandwiches)
        student_queue = collections.deque([(s, False) for s in students])

        while student_queue:

            student_pref, student_seen = student_queue.popleft()

            if student_pref == sandwich_queue[0]:
                sandwich_queue.popleft()
                ans += 1

            elif not student_seen:
                student_queue.append((student_pref, True))

            elif student_seen and student_pref != sandwich_queue[0]:
                break

            print(student_queue)
            print(sandwich_queue)
            print()

        return ans
