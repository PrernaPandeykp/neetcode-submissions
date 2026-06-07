class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for l,m in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(i+l, j+m)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count +=1
            
        return count
        