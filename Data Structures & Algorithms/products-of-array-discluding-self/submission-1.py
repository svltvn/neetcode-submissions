class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productNums = [0] * len(nums)
        
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i!=j:
                    product *= nums[j]
            productNums[i] = product
        return productNums

