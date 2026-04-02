class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        n = len(candidates)
        def backtrack(i, total):
            if total == target:
                res.append(sol.copy())
                return
            if i== n or total > target:
                return
            sol.append(candidates[i])
            backtrack(i,total + candidates[i])
            sol.pop()
            backtrack(i+1,total)
        backtrack(0,0)
        return res
