class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def surround(x, y):
            nonlocal board, visited
            if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and board[x][y] == "O":
                visited.add((x, y))
                board[x][y] = "T"
                for dx, dy in neighbours:
                    surround(x + dx, y + dy)

        # check for any islands touching the edges
        for i in range(0, m):
            if board[i][0] == "O":
                surround(i, 0)
            if board[i][n-1] == "O":
                surround(i, n-1)
        for j in range(0, n):
            if board[0][j] == "O":
                surround(0, j)
            if board[m-1][j] == "O":
                surround(m-1, j)

        for u in range(0, m):
            for v in range(0, n):
                if board[u][v] == "T":
                    board[u][v] = "O"
                else:
                    board[u][v] = "X"

        
        
