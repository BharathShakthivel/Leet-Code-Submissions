class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        total = sum(matchsticks)
        
        if total%4 !=0:
            return False
        side = total // 4
        sides = [0] * 4
        def backtrack(i):
            if i == n:
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
                    if sides[j] == 0:
                        break
            return False
        return backtrack(0)


