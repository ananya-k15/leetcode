class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # exchange the rows of the matrix 
        m, n = len(matrix), len(matrix[0])
        mid = m // 2
        for x in range(mid):
            prev, curr = x, m-1-x
            for y in range(0, n):
                temp = matrix[x][y]
                matrix[x][y] = matrix[m-1-x][y]
                matrix[m-1-x][y] = temp

        for i in range(0, m):
            for j in range(0, n):
                if i < j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp