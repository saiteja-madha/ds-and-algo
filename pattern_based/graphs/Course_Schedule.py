# https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            visit.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            preReq[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


# Example 1
numCourses = 2
prerequisites = [[1, 0]]
assert Solution().canFinish(numCourses, prerequisites) is True

# Example 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
assert Solution().canFinish(numCourses, prerequisites) is False
