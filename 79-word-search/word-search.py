class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        def backtrack(x, y, current):
            # print(current, x, y, word)
            # base case = return True if current matches word
            if current == word:
                # print("returning true")
                return True
            # for all possible vertical and horizontal neighbours
            for dx, dy in neighbours:
                # prune if indices are invalid
                nx, ny = x + dx, y + dy
                # print(nx, ny, visited)
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                # prune if current's letter does not match the 
                # corresponding letter in word
                if board[nx][ny] != word[len(current)]:
                    continue
                visited.add((nx, ny))
                # otherwise, backtrack
                if backtrack(nx, ny, current + board[nx][ny]):
                    return True
                # remove this letter and explore other neighbours
                visited.remove((nx, ny))
            # return False if no backtracking possibility worked
            return False
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if backtrack(i, j, word[0]):
                        return True
                    visited.remove((i, j))
        return False
