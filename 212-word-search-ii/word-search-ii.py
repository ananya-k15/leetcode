class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_set = set()
        for word in words:
            for i in range(1, len(word)+1):
                prefix_set.add(word[:i])
        word_set = set(words)

        results = []
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])
        visited = set()

        def backtrack(current, i, j):

            val = "".join(current)

            if val not in prefix_set:
                return

            if val in word_set:
                # print("here", current)
                word_set.remove(val)
                results.append(val)
                
            for dx, dy in neighbours:
                x, y = i + dx, j + dy
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited:
                    visited.add((x, y))
                    current.append(board[x][y])
                    backtrack(current, x, y)
                    current.pop()
                    visited.remove((x, y))

        for di in range(m):
            for dj in range(n):
                visited.add((di, dj))
                backtrack([board[di][dj]], di, dj)
                visited.remove((di, dj))

        return results

