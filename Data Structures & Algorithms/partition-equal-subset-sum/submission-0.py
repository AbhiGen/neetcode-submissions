class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=sum(nums)
        if totalsum%2==1:
            return False
        n=len(nums)
        target=sum(nums)//2
        dp=[[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,n+1):
            current=nums[i-1]
            for j in range(1,target+1):
                if j<current:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-current]
        return dp[n][target]

        