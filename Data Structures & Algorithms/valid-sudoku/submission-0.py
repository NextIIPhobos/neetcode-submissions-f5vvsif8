class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_i = set()
            set_j = set()
            for j in range(9):
                if board[i][j].isdigit() and int(board[i][j]) in set_i:
                    return False
                else: 
                    if board[i][j].isdigit():
                        set_i.add(int(board[i][j])) 
                if board[j][i].isdigit() and int(board[j][i]) in set_j:
                    return False
                else: 
                    if board[j][i].isdigit():
                        set_j.add(int(board[j][i])) 
        for i in range(0, 8, 3):
            for j in range(0,8,3):
                set_block = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isdigit() and int(board[i+k][j+l]) in set_block:
                            return False
                        else: 
                            if board[i+k][j+l].isdigit(): 
                                set_block.add(int(board[i+k][j+l]))
        return True
