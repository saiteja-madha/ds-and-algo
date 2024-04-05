# https://leetcode.com/problems/course-schedule-ii/

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []

        finish = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in finish:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            finish.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output


# Example 1
numCourses = 2
prerequisites = [[1, 0]]
assert Solution().findOrder(numCourses, prerequisites) == [0, 1]

# Example 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
assert Solution().findOrder(numCourses, prerequisites) == []
