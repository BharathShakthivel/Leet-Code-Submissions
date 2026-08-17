class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down
        # n =  len(cost)
        # dp = [0] * (n+1)
        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[n]

        # Bottom Up
        # We add a extra element which is natrually zero to indicate as the target to achieve
        # We don't take xtra memory so the Space Complexity is O(1) and Time is O(n) as we iterate only once.

        # We come from reverse and start at the third element all the way to first element after adding the target elemet zero.

        #  Eg [10,15,20,0]
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
        # We put -1 at stop because python doesn't consider last element in range
        # -1 for reverse step count
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        # We start either from first or second position, so the min of those elements should be the min cost to reach the target.
        return min(cost[0],cost[1])


