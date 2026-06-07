from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        ans = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for child in adj[node]:
                dfs(child)

            return True
 
        for i in range(n):
            if dfs(i) and i in visited:
                ans+=1

        return ans

        



        

