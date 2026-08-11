"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution():
    def climbStairs(self, n):
        def climb(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            return climb(n-1) + climb(n-2)

        return climb(n)

    def climbStairs2(self,n):
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:
                return memo[n]

            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]

        return climb(n)

    def climbStairs3(self, n):
        if n <= 2: return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i-2]

        return dp[n]

solution = Solution()
#print(solution.climbStairs(15))
print(solution.climbStairs2(4))
#print(solution.climbStairs3(15))


# dictio = {}
# dictio[1] = 1
# dictio[2] = 2

# n = 55

# dictio[n] = 8

# print(dictio)