class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            if i >= ROWS or j >= COLS or i<0 or j<0 or board[i][j]== 'X' or board[i][j]== 'S':
                return
            board[i][j] = 'S'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        if board:
            ROWS = len(board)
        if board[0]:
            COLS = len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS-1 or j ==0 or j == COLS-1) and board[i][j] == 'O':
                    dfs(i,j)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'S':
                    board[i][j] = 'O'

