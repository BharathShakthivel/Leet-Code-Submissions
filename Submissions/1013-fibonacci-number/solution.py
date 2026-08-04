class Solution:
    def fib(self, n: int) -> int:
        # Normal Recurrsion
        # if n ==0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-2) + self.fib(n-1)

        # Top Down Dynamic Programming - Memoisation - Time - O(n); Space - O(n)
        
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # memo = {0:0,1:1}
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = f(x-2) + f(x-1)
        #         return memo[x]
        # return f(n)
        
        # Bottom Up Dynamic Programming - Tabulation - Time - O(n); Space - O(n)

        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0],dp[1] = 0,1
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

        # Bottom Up Dynamic Programming - Tabulation - Time - O(n); Space - O(1)

        if n == 0:
            return 0
        if n == 1:
            return 1
        prev,cur = 0,1
        for i in range(2,n+1):
            prev,cur = cur, prev+cur+i
        return cur
