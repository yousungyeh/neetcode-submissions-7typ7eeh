class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        earn_list = []
        for i in range(l):
            for j in range(i+1, l):
                if prices[j]>prices[i]:
                    earn_list.append(prices[j]-prices[i])
        if not earn_list:
            return 0
        return max(earn_list)

