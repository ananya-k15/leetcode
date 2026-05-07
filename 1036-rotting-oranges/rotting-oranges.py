class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        queue = deque([])
        maxTime = 0

        def rot():
            nonlocal grid, visited, queue, maxTime
            if len(queue) == 0:
                return 
            x, y, time = queue.popleft()
            if (x, y) not in visited and grid[x][y] == 2:
                visited.add((x, y))
                maxTime = max(time, maxTime)
                for dx, dy in neighbours:
                    if x+dx >= 0 and x+dx < m and y+dy >= 0 and y+dy < n:
                        if (x + dx, y + dy) not in visited and grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 2
                            queue.append((x + dx, y + dy, time+1))
            rot()

        # traverse the entire grid, looking for rotten oranges
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    # begin rotting the oranges at time=0
                    # for di, dj in neighbours:
                    #     queue.append((i + di, j + dj, 1))
        rot()

        # if there is a fresh orange left, return -1
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    return -1

        # else return maxTime
        return maxTime