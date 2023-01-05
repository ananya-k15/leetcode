class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        drow = { x:set() for x in range(0, 9, 1)}
        dcol = { y:set() for y in range(0, 9, 1)}
        dblock = dict()
        for u in range(0, 3, 1) :
            for v in range(0, 3, 1) :
                key = str(u) + str(v)
                dblock[key] = set()
        for i in range(0, 9, 1) :
            for j in range(0, 9, 1) :
                num = board[i][j]
                key = str(i//3) + str(j//3)
                if num == '.' : 
                    continue
                elif num in drow[i] or num in dcol[j] or num in dblock[key] :
                    return False
                else : 
                    drow[i].add(num)
                    dcol[j].add(num)
                    dblock[key].add(num)
        return True
    
        # for row in board : 
        #     drow = set()
        #     for num in row : 
        #         if num != "." and num in drow :
        #             return False
        #         elif num != "." : 
        #             drow.add(num)
        # # check each col
        # for i in range(0, 9, 1) : 
        #     dcol = set()
        #     for j in range(0, 9, 1) : 
        #         num = board[i][j]
        #         if num != "." and num in dcol :
        #             return False
        #         elif num != "." : 
        #             dcol.add(num)
    