class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Time : 2^n ; Space: O(n!)

        res,sol = [],[]
        n = len(s)
        # We are going through evrysub string and checking if it is palindrone,

        def is_pali(s, l ,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l,r = l+1, r-1
            return True

        def backtrack(i):
            if i == n:
                # Base case - if we go out of balance, then we add whatever palindrome substrings in sol to res
                res.append(sol[:])
                return # We backtrack after adding a sol to res
            for j in range(i,n):
                if is_pali(s,i,j):
                    # We only add if the sub string is palindrome
                    sol.append(s[i:j+1])
                    # We append the string and backtrack till we find set of valid combinations of subtstrings
                    backtrack(j+1)
                    sol.pop()
                    # We pop the last element and start from next index.
        backtrack(0) # Start from the zeroth position of the index.
        return res
            
