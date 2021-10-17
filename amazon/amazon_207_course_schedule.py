"""
- Finding a valid schedule dependencies is to find if there's no cycle in the graph
"""


from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = collections.defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False

        return True

    def isCyclic(self, currCourse, courseDict, checked, path):

        if checked[currCourse]:
            return False

        if path[currCourse]:
            return True

        path[currCourse] = True

        ret = False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret:
                break

        path[currCourse] = False
        checked[currCourse] = True

        return ret

