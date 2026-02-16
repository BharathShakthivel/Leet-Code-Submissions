class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Optimal Approach

        """
        VALID SUDOKU - Single Pass Solution

        LOGIC:
        - Use 3 hash maps (rows, cols, squares) to track seen digits
        - Each hash map: key -> set of digits seen in that row/col/square
        - Iterate through board once, checking all 3 constraints simultaneously
        - If digit already exists in current row/col/square -> invalid
        - Otherwise add digit to all 3 tracking sets

        STEPS:
        1. Create 3 defaultdict(set): rows, cols, squares
        2. Loop through each cell (r, c) in 9x9 board
        3. Skip empty cells "."
        4. Check if current digit exists in:
        - rows[r] (current row)
        - cols[c] (current column)  
        - squares[(r//3, c//3)] (current 3x3 box)
        5. If found in any -> return False (duplicate detected)
        6. Add digit to all 3 sets: rows[r], cols[c], squares[(r//3, c//3)]
        7. If loop completes -> return True (no duplicates found)

        KEY INSIGHT:
        - Box identification: (r//3, c//3) maps any cell to its 3x3 sub-box
        Example: cell (5,7) -> box (1,2) [middle-right box]

        TIME: O(1) - fixed 9x9 board = 81 cells
        SPACE: O(1) - max 9 sets × 3 categories × 9 elements
    """
        # OPTIMAL APPROACH
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True


        # # INITIAL APPROACH
        
        # total_len = len(board)
        # dict_validation = {}
        # #Row wise check
        # for i in board:
        #     for j in i:
        #         if j != ".":
        #             dict_validation[j] = 1 + dict_validation.get(j,0)
        #     for n,c in dict_validation.items():
        #         if c > 1:
        #             return False
        #     dict_validation = {}
        
        # #Column wise check
        # col_ptr = 0
        # while col_ptr!= total_len:
        #     for i in board:
        #         if i[col_ptr] != ".":
        #             dict_validation[i[col_ptr]] = 1 + dict_validation.get(i[col_ptr],0)
        #     for n,c in dict_validation.items():
        #         if c > 1:
        #             return False
        #     dict_validation = {}
        #     col_ptr+=1
        # # Squares Check
        # squares = collections.defaultdict(set)
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if board[r][c] in squares[(r//3,c//3)]:
        #             return False
        #         squares[(r//3,c//3)].add(board[r][c])
        # return True
