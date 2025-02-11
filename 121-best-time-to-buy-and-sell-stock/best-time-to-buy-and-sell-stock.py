class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        l,r=0,1
        while l<len(prices) and r<len(prices):
            if prices[r]<prices[l]:
                l=r
                r+=1
            elif prices[r]>prices[l]:
                sol = max(sol,prices[r]-prices[l])
                r+=1
            else:
                r+=1
        return sol
