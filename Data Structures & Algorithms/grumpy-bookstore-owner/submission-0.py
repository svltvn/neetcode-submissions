class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sumCust1 = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])
        maxSum = sumCust1
        l, r = 0, minutes
        while r <= len(customers): 
            sumCust2 = sum([customers[i] for i in range(l,r,1) if grumpy[i] == 1])
            maxSum = max(maxSum, sumCust1+sumCust2)
            print(sumCust1,sumCust2,customers[l:r])
            l+=1
            r+=1
        return maxSum