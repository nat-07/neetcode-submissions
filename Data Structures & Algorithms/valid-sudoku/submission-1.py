class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        # There will only ever be 9 rows and 9 columns
        # We can index the squares by dividing the row and column by 3 and rounding them down
        for row in range (9): 
            for col in range (9):
                if board[row][col] != ".":
                    square = (row // 3,col // 3)
                    value = board[row][col]
                    if (value in squares[square] or value in rows[row] or value in cols[col]):
                        return False
                    else: 
                        rows[row].append(value)
                        cols[col].append(value)
                        squares[square].append(value)
        return True
