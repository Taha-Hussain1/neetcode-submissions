class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        bp = prices[0]
        sp = prices[0]
        for i in range(len(prices)):
            if prices[i] <= bp:
                profits.append(sp - bp)
                bp = prices[i]
                sp = prices[i]
            elif prices[i] > sp:
                sp = prices[i]
        profits.append(sp - bp)
        return max(profits)











        increment = 0
        for price1 in prices:
            increment += 1
            for price2 in prices[increment:]:
                price_diff = price2 - price1
                profits.append(price_diff)
        if not profits:
            return 0
        if max(profits) < 0:
            return 0
        return max(profits)


