class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArray = [0] * len(nums)
        
        for i in range(len(nums)):
            numPop = nums.pop(i)
            product = 1
            for num in nums:
                product *= num
            productArray[i] = product
            nums.insert(i, numPop)
        return productArray

        