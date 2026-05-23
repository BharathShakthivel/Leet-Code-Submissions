class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        fresh = 0
        ROWS,COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        #  Edge Case - No Rotten Oranges
        if not fresh:
            return 0
        # Helper Function
        def all_direction(i,j):
            nonlocal fresh
            if i >= ROWS or j >= COLS or i < 0 or j < 0 or grid[i][j] == 0 or grid[i][j] == 2:
                return
            grid[i][j] = 2
            fresh-=1
            q.append((i,j))

        # Main - Breadth First Search
        minutes = 0
        while q:
            for i in range(len(q)):
                rotten_row, rotten_col = q.popleft()
                grid[rotten_row][rotten_col] = 2
                all_direction(rotten_row+1,rotten_col)
                all_direction(rotten_row,rotten_col+1)
                all_direction(rotten_row-1,rotten_col)
                all_direction(rotten_row,rotten_col-1)
            if q:
                minutes+=1
        
        #  Checking if still fresh oranges are left
        if fresh>0:
                return -1
        return minutes


