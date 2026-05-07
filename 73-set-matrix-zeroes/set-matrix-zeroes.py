class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = []
        cols = []
        rowZero = False
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(0, m):
                matrix[i][0] = 0
        if rowZero == True:
            for j in range(0, n):
                matrix[0][j] = 0

