class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # while exploring
        def explore(x, y):
            nonlocal seen, m, n, grid
            # check north, south, east and west only
            # if we hit an seen 1 or 0 -> return
            # if we hit invalid indices -> return
            if (x >= 0 and x < m) and (y >= 0 and y < n) and ((x, y) not in seen) and grid[x][y] == "1":
                grid[x][y] = "0"
                # if we hit an unseen 1 -> recursively explore that 1
                explore(x+1,y)
                explore(x,y+1)
                explore(x-1,y)
                explore(x,y-1)
            return

            
        islandCount = 0
        seen = set()
        m, n = len(grid), len(grid[0])

        # we traverse the grid to find a 1
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                # print(seen)
                if grid[i][j] == "0":
                    continue
                # once we hit a one -> we've got an island
                else:
                    # append islandCount
                    islandCount += 1
                    # explore all neighbours to check island area
                    # add all 1's discovered this way to a set of seen 1's
                    explore(i, j)
    
        return islandCount