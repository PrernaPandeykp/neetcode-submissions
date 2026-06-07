class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
            # adj[v].append(u)

        visitedSet = set()
        def dfs(node):
            if node in visitedSet:
                return False
            if adj[node] == []:
                return True

            visitedSet.add(node)
            for i in adj[node]:
                if not dfs(i):
                    return False

            visitedSet.remove(node)
            adj[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
