class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # 1. Initialize grid (m x n)
        dp = [[0] * n for _ in range(m)]
        
        # 2. Base case: There is exactly 1 way to be at the starting point
        dp[0][0] = 1
        
        # 3. Move FORWARD from top-left to bottom-right
        for i in range(m):
            for j in range(n):
                # If we can look up to our top neighbor
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                # If we can look left to our left neighbor
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
                    
        # 4. The final accumulated answer is now at the destination corner
        return dp[m - 1][n - 1]

            