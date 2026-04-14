class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prefix min
        """
        max_earn = 0
        seen_lowest_price = prices[0]
        for p in prices:
            if p > seen_lowest_price:
                # sell
                max_earn = max(max_earn, p - seen_lowest_price)
            if p < seen_lowest_price:
                seen_lowest_price = p
        return max_earn