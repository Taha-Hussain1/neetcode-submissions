class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r // 3, c // 3)
        # check rows
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in "123456789":
                    return False
                if ( 
                    board[row][col] in cols[col] or 
                    board[row][col] in rows[row] or 
                    board[row][col] in squares[(col // 3, row // 3)]
                ):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(col // 3, row // 3)].add(board[row][col])


        return True

