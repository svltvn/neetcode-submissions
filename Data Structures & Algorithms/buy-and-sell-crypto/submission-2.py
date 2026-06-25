class Solution:
    '''
    Revisiting after sometime, will try BF and then SW
    '''
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit



        