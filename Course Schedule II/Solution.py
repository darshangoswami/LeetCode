class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for pre in adjList[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res