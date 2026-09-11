class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
            
        # 1. Get a sorted, unique version of the array
        # WHY: An increasing subsequence must follow sorted order. 
        # The LIS is just the Longest Common Subsequence between the original array and this sorted one.
        text1 = nums
        text2 = sorted(list(set(nums)))
        
        m, n = len(text1), len(text2)
        
        # 2. Create the 2D DP Grid initialized with zeros
        # Dimension is (m + 1) x (n + 1) to account for empty string base cases.
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 3. Fill the grid row by row
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # If the numbers match, we extend the sequence
                if text1[i - 1] == text2[j - 1]:
                    # WHY: Add 1 to the best result found *before* these two numbers (diagonally top-left).
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    
                # If they don't match, carry over the best choice found so far
                else:
                    # WHY: Take the max from either skipping the current item in text1 (above)
                    # or skipping the current item in text2 (left).
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # 4. The final answer accumulates in the bottom-right corner
        return dp[m][n]

            