class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        mincost=prices[0]
        for i in prices:
            maxprofit=max(maxprofit,i-mincost)
            mincost=min(mincost,i)
        return maxprofit
        