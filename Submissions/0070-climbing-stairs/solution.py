class Solution:
    def climbStairs(self, n: int) -> int:
        #  Basically adding the ways to reach the target through Bottom up Approach 
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one= one + two
            two = temp
        return one
