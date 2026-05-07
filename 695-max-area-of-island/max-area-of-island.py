class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(x, y):
            area = 0
            if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and grid[x][y] == 1:
                visited.add((x, y))
                grid[x][y] = 0
                area += 1
                for dx, dy in neighbours:
                    area += dfs(x + dx, y + dy)
            return area
        maxArea = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea