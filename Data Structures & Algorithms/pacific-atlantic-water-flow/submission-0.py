class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        grid = [["" for i in range(cols)] for i in range(rows)]
        res = []
        def dfs(i,j, ocean):
            if i<0 or i>= rows or j<0 or j>=cols:
                return 

            if ocean in grid[i][j]:
                return

            grid[i][j] +=ocean
            for a, b in [(0,1),(1,0), (0,-1), (-1,0)]:
                x,y = i+a, j+b
                if x<0 or y<0 or x >=rows or y >=cols or heights[x][y] <heights[i][j] or ocean in grid[x][y]:
                    continue
                
                dfs(i+a, j+b, ocean)

        for j in range(cols):
            dfs(0, j, 'p')
            dfs(rows-1, j,'a')

        for i in range(rows):
            dfs(i, 0, 'p')
            dfs( i, cols-1,'a')

        for r in range(rows):
            for c in range(cols):
                if 'a' in grid[r][c] and 'p' in grid[r][c]:
                    res.append([r,c])

        return res