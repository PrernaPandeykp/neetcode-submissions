class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for n in adj[node]:
                if n == prev:
                    continue

                if not dfs(n, node):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n

                







        

