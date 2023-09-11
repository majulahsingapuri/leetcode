class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = {}
        for i in range(numCourses):
            deps[i] = []

        for cou, pre in prerequisites:
            deps[cou].append(pre)

        visited = set()
        res = []

        def dfs(course):
            if course in visited:
                return False
            if deps[course] == []:
                if course not in res:
                    res.append(course)
                return True
            visited.add(course)
            for dep in deps[course]:
                if not dfs(dep): return False
            visited.remove(course)
            deps[course] = []
            res.append(course)
            return True

        for course in deps.keys():
            if not dfs(course): return []
        
        return res
        