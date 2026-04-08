class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # Time k * n!/(n-k)! * k!   ; Space: O(N)
        res,sol = [],[]
        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])  #Taking a copy of the solution
                return
            for j in range(i,n+1): # We go all the way till n + 1 and including N
                sol.append(j)
                backtrack(j+1)
                sol.pop()
        backtrack(1) # We start from 1 as it is mentioned in the problem
        return res

            
