from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False]*n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(node):
            for ele in adj[node]:
                if not visited[ele]:
                    visited[ele] = True
                    dfs(ele)

        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1
        return res

