class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        suffix max
        """
        l = len(prices)
        suffix = [0]*l
        suffix[-1] = prices[-1]
        for i in range(l-2, -1, -1):
            suffix[i] = max(suffix[i+1], prices[i])
        max_earn = 0
        for i in range(l):
            earn = suffix[i]-prices[i]
            max_earn = max(max_earn, earn)
        return max_earn