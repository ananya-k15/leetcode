class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def backtrack(x, y, idx):
            # base case = return True if current matches word
            if idx == len(word):
                return True
            # for all possible vertical and horizontal neighbours
            for dx, dy in neighbours:
                # prune if indices are invalid
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                # prune if current's letter does not match the 
                # corresponding letter in word
                if board[nx][ny] != word[idx]:
                    continue
                temp = board[nx][ny]
                board[nx][ny] = 0
                # otherwise, backtrack
                if backtrack(nx, ny, idx + 1):
                    return True
                # remove this letter and explore other neighbours
                board[nx][ny] = temp
            # return False if no backtracking possibility worked
            return False

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if backtrack(i, j, 1):
                        return True
                    board[i][j] = temp

        return False
