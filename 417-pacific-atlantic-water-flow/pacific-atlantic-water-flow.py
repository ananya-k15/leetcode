class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Key idea: instead of flowing downhill, flow uphill
        # create two sets: one for nodes reachable by each ocean
        # then return intersecton of those sets
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # modified dfs to explore nodes reachable by each ocean
        def explore(x, y, ocean):
            ocean.add((x, y))
            # for each direction NSEW
            for a, b in dirs:
                nx, ny = x+a, y+b
                # only call explore on valid indices
                if (0 <= nx < m) and (0 <= ny < n):
                    # if we can flow uphill to this unseen node, explore it
                    if (heights[nx][ny] >= heights[x][y]) and ((nx, ny) not in ocean):
                        explore(nx, ny, ocean) 

        # traverse the first row + first column to start off pacific set
        for i in range(m):
            explore(i, 0, pacific)
        for j in range(n):
            explore(0, j, pacific)
        
        # traverse the last row + last column to start off atlantic set
        for i in range(m):
            explore(i, n-1, atlantic)
        for j in range(n):
            explore(m-1, j, atlantic)

        result = pacific & atlantic
        return list(result)