class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {x:set() for x in range(0, 9, 1)}
        columns = {y:set() for y in range(0, 9, 1)}
        box_ind = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        subbox = {z:set() for z in box_ind}
        
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                val = board[i][j]
                if val == '.':
                    continue
                else:
                    box = str(int(i // 3)) + str(int(j // 3))
                    if val in rows[i] or val in columns[j] or val in subbox[box]:
                        return False 
                    else:
                        rows[i].add(val)
                        columns[j].add(val)
                        subbox[box].add(val)
        
        return True

