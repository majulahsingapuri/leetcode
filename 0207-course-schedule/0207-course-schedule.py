class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = {}
        for i in range(numCourses):
            deps[i] = []

        for cou, pre in prerequisites:
            deps[cou].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if deps[course] == []:
                return True
            visited.add(course)
            res = True
            for i, dep in enumerate(deps[course]):
                res = res and dfs(dep)
                deps[course].pop(i)
            visited.remove(course)
            return res

        for course in deps.keys():
            if not dfs(course): return False
        
        return True
        