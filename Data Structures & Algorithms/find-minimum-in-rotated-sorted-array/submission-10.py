class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Done this problem before, but let's try to attempt it again

        BF - very simple, but how would we do binary, w/o using min and max functions
        '''


        l, r = 0, len(nums)

        if len(nums) == 1:
            return nums[0]

        while l<r:
            m = (r-l)//2 +l

            num1 = nums[l:m]
            num2 = nums[m:r]
            print(num1, num2)

            if num1 == sorted(num1) and num2 == sorted(num2):
                return min(num1[0], num2[0])
            elif num1 != sorted(num1):
                r = m+1
            else:
                l = m
                


        