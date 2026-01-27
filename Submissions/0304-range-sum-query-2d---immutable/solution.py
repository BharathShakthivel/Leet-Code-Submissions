class NumMatrix:
    # Worst Case Solution - O(n * n)
    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * cols for row in range(rows)]
        for i in range(rows):
            for j in range(cols):
                top = self.prefix[i-1][j] if i > 0 else 0
                left = self.prefix[i][j-1] if j > 0 else 0
                diag = self.prefix[i-1][j-1] if i > 0 and j > 0 else 0
                self.prefix[i][j] = matrix[i][j] + top + left - diag
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # sum_val = 0
        # for i in range(row1,row2+1):
        #     for j in range(col1,col2+1):
        #         sum_val+=self.matrix[i][j]
        # return sum_val
        total = self.prefix[row2][col2]
        top = self.prefix[row1-1][col2] if row1>0 else 0
        left = self.prefix[row2][col1-1] if col1>0 else 0
        diag = self.prefix[row1-1][col1-1] if row1>0 and col1>0 else 0
        return total - top - left + diag

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
