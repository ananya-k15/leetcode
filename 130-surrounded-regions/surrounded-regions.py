class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find all non surrounded regions
        # start exploring from the edges and create a set for all such nodes
        # finally, traverse the board and mark everything not in the set as 'X'
        surrounded = set()
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def explore(x, y):
            nonlocal surrounded
            # if (x, y) in surrounded:
            #     return
            # check for invalid indices
            if (0 <= x < m) and (0 <= y < n):
                if board[x][y] == "O":
                    surrounded.add((x, y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if (nx, ny) not in surrounded:
                            explore(nx, ny)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if (i, j) not in surrounded:
                        explore(i, j)

        for i in range(m):
            for j in range(n):
                if (i, j) not in surrounded:
                    board[i][j] = "X"

        