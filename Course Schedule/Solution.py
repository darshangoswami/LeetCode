class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adjMap[crs] == []:
                return True

            visited.add(crs)
            for pre in adjMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adjMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True