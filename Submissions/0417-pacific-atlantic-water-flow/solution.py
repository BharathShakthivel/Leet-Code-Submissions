class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        pacific_set = set()
        atlantic_set = set()
        ROWS,COLS = len(heights),len(heights[0])
        def dfs(i,j,visit,prev):
            if (i,j) in visit or i < 0 or j < 0 or i == ROWS or j == COLS or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        for c in range(COLS):
            dfs(0,c,pacific_set,heights[0][c])
            dfs(ROWS-1,c,atlantic_set,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,pacific_set,heights[r][0])
            dfs(r,COLS-1,atlantic_set,heights[r][COLS-1])
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific_set and (i,j) in atlantic_set:
                    result.append((i,j))
        return result
        
        


