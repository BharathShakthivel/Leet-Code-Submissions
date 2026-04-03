class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, sol = [],[]
        n = len(candidates)
        def backtrack(i,total):
            if total == target:
                res.append(sol[:])
                return
            if total > target or i == n:
                return
            for j in range(i,n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > (target - total):
                    break           
                sol.append(candidates[j])
                backtrack(j+1,total+candidates[j])
                sol.pop()
        backtrack(0,0)
        return res
