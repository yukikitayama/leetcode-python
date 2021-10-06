"""
Example
- employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
- make a hashmap with key employee id and value employee importance



Algorithm
- We need recursive algorithm to get subordinates until no more subordinates
- Initialize ans to 0
- Get employee[id].importance, and add it to ans
- Get subordinates[id],
- For each subordinate, add its importance to ans
- Get
"""


from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int):

        # id_to_importance = {}
        # for employee in employees:
        #     id_to_importance[employee.id] = employee.importance
        id_to_employee = {employee.id: employee for employee in employees}

        def dfs(id):
            employee = id_to_employee[id]
            return employee.importance + sum(dfs(id) for id in employee.subordinates)

        return dfs(id)


employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, [])
]
id = 1
print(Solution().getImportance(employees, id))


