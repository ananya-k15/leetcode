class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        # we cover the first row, then the last column, then the last row, then the opposite of the first column
        # we can keep track of the ending points using horizontal/vertical pointers
        
        vi, vj = 0, len(matrix) # m-1
        hi, hj = 0, len(matrix[0]) # n-1
        spiral = []

        while vi < vj and hi < hj:

            # first row
            # matrix[vi][hi] to matrix[vi][hj]
            spiral += matrix[vi][hi:hj]
            # print("1", spiral)
            # last column
            # matrix[vi+1][hj] to matrix[vj][hj]
            for x in range(vi+1, vj-1):
                spiral.append(matrix[x][hj-1])
            # print("2", spiral)
            # last row in opposite order
            if vi != vj-1:
                spiral += matrix[vj-1][hi:hj][::-1]
            # print("3", spiral)
            # first column in opposite order
            if hi != hj-1:
                for x in range(vj-2, vi, -1):
                    spiral.append(matrix[x][hi])
            # print("4", spiral)
            vi += 1
            vj -= 1
            hi += 1
            hj -= 1

        return spiral