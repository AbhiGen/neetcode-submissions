class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         
        # takes O(1) time, making the code much faster.
        word_set = set(wordDict)
        
        # WHY: dp[i] will be True if the substring s[0:i] can be broken into valid words.
        # We need a size of len(s) + 1 to account for the empty string base case.
        dp = [False] * (len(s) + 1)
        
        # BASE CASE: An empty string is always valid (trivially breakable).
        dp[0] = True
        
        # WHY: i tracks the end of the current substring we are testing (s[0:i]).
        for i in range(1, len(s) + 1):
            # WHY: j scans all possible split points before i.
            for j in range(i):
                
                # THE LOGIC: 
                # 1. dp[j] must be True (the prefix s[0:j] is already a valid word blend).
                # 2. s[j:i] must exist in our dictionary (the suffix is a valid word).
                if dp[j] and s[j:i] in word_set:
                    # If both are true, the whole chunk s[0:i] becomes valid!
                    dp[i] = True
                    break # WHY: Once we know s[0:i] is valid, we can stop checking other split points.
                    
        # WHY: dp[len(s)] holds the answer for the entire string.
        return dp[len(s)]
