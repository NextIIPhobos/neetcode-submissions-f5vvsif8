class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)*len(board[0]) < len(word): return False
        flag = False

        def func(i,j,c, prevs):
            if c == len(word):
                nonlocal flag
                flag = True
                return
            
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if k >= 0 and k < len(board) and l >= 0 and l < len(board[0]):
                        if (k == i - 1 and l == j-1) or (k == i - 1 and l == j+1) or (k == i + 1 and l == j-1) or (k == i + 1 and l == j+1) or (k==i and l==j) or ([k,l] in prevs):
                            continue
                        print(k,l)
                        if board[k][l] == word[c]:
                            print(board[k][l])
                            
                            func(k,l,c+1,prevs + [[i, j]])
            return
        
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    print(board[i][j])
                    func(i,j,1,[[i,j]])
        
        return flag

        
        