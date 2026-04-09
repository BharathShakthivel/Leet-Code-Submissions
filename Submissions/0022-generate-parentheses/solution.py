class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol,res = [],[]

        def backtrack(open_n,close_n):
            if open_n == close_n == n:
                res.append("".join(sol))
            if open_n < n:
                sol.append("(")
                backtrack(open_n+1,close_n)
                sol.pop()
            if close_n < open_n:
                sol.append(")")
                backtrack(open_n,close_n+1)
                sol.pop()
        backtrack(0,0)
        return res
            

