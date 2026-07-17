class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square ={}
        for i in range (9): 
            row[i] = []
            
            for j in range (9): 
                index = (i // 3) * 3 + (j // 3)
                if board[i][j] != ".":
                    if index in square:
                        if board[i][j] in square[index]:
                            return False
                        else:

                            square[index].append(board[i][j])
                    else:
                        square[index] = [board[i][j]]
                    if j in col:
                        if board[i][j] in col[j]:
                           
                            return False
                        else:
                            col[j].append(board[i][j])
                    else: 
                        col[j] = [board[i][j]]
                    if (board[i][j] in row[i]): 
                        
                        return False
                    else: 
                        row[i].append(board[i][j])
                       
        return True
        
