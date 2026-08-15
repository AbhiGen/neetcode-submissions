class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen=set(s)
        res=0
        for i in seen:
            count=0
            left=0
            for right in range(len(s)):
                if s[right]==i:
                    count+=1
                while (right-left+1)-count>k:
                    if s[left]==i:
                        count-=1
                    left+=1
                res=max(res,right-left+1)
        return res
        
        