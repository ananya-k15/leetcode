class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and grid[x][y] == "1":
                visited.add((x, y))
                grid[x][y] = "0"
                for dx, dy in neighbours:
                    dfs(x + dx, y + dy)
        islands = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
                
                
            