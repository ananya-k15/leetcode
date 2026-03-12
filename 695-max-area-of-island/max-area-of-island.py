class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandArea = 0 # default case
        m, n = len(grid), len(grid[0])

        # We use a modified version of DFS to explore each island
        # It should return the number of 1's in the islands, i.e., area
        def explore(x, y):
            # nonlocal m, n, grid
            # if indices are valid or it's a 1, 
            # explore all horizontal and vertical neighbors 
            if (x >= 0 and x < m) and (y >= 0 and y < n) and grid[x][y] == 1:
                # mark this as 0 since we've visited it!
                grid[x][y] = 0
                # return 1 + sum of 1's from neighbor exploration
                return 1 + explore(x+1, y) + explore(x-1, y) + explore(x, y+1) + explore(x, y-1)
            # otherwise return 0
            return 0
        
        # Traverse the entire grid
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                # When we hit an island, i.e, a '1'
                if grid[i][j] == 1:
                    # Call explore to get island's area
                    area = explore(i, j)
                    # Compare this island to the maxIslandArea
                    maxIslandArea = max(maxIslandArea, area)

        # return max island area
        return maxIslandArea