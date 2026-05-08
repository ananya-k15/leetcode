class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(i, j, board):
            x = i
            # check for a queen in the same column
            while x >= 0:
                if board[x][j] == "Q":
                    return False
                x -= 1
            # check along left diagonal
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                if board[x][y] == "Q":
                    return False
                x -= 1
                y -= 1
            # check along right diagonal
            x, y = i - 1, j + 1
            while x >= 0 and y < len(board):
                if board[x][y] == "Q":
                    return False
                x -= 1
                y += 1
            return True

        board = [["." for x in range(n)] for x in range(n)]
        results = []
        def backtrack(i):
            if i == n:
                copy = ["".join(row) for row in board]
                results.append(copy)
                return
            
            for j in range(0, n):
                if isSafe(i, j, board):
                    board[i][j] = "Q"
                    backtrack(i+1)
                    board[i][j] = "."
        
        backtrack(0)
        return results