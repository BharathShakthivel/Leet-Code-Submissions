class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat matrix as:
        # 1. Sorted rows
        # 2. Rows ordered by first element
        #
        # Step 1: Binary search to find candidate row.
        # Step 2: Binary search inside that row.
        #
        # If found → True
        # Else → False

        ROWS = len(matrix)
        top,bot = 0, ROWS-1
        while top<=bot:
            mid_row = (top + bot)//2
            if matrix[mid_row][0]<= target and matrix[mid_row][-1]>= target:
                l,r = 0, len(matrix[mid_row])-1
                while l<=r:
                    cur_mid = (l+r) // 2
                    if target > matrix[mid_row][cur_mid]:
                        l = cur_mid + 1
                    elif target < matrix[mid_row][cur_mid]:
                        r = cur_mid - 1
                    else:
                        return True
                return False
            elif matrix[mid_row][0]> target:
                bot = mid_row-1
            else:
                top = mid_row+1
        return False


        # The matrix has two important properties:
        # 1. Each row is sorted.
        # 2. The first element of each row is greater than the last element of the previous row.
        #
        # This means:
        # - Rows are sorted internally.
        # - Rows themselves are ordered relative to each other.
        #
        # So we can apply binary search twice:
        #   Step 1 → Binary search to find the correct row.
        #   Step 2 → Binary search inside that row.

        # We search for the row that could contain the target.
        #
        # For a given mid_row:
        # - If target is between the first and last element of this row,
        #     → This is the row where target must be.
        # - If target is smaller than the first element of mid_row,
        #     → Target must be in rows above.
        # - Otherwise,
        #     → Target must be in rows below.
        #
        # This reduces row search space by half each time.

        # Once we identify the correct row,
        # perform a normal binary search on that row.
        #
        # Standard binary search logic:
        # - If mid element < target → search right half
        # - If mid element > target → search left half
        # - If equal → return True
        #
        # If search ends → target not present → return False

        # Binary search on rows → O(log m)
        # Binary search inside row → O(log n)
        # Total = O(log m + log n)


 
