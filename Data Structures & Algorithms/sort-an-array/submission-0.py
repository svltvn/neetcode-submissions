class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
            else:
                return nums
        else:
            split = len(nums)//2
            nums1 = self.sortArray(nums[:split])
            nums2 = self.sortArray(nums[split:])
            
            p1, p2 = 0,0
            for i in range(len(nums)):
                num1 = 50001
                num2 = 50001
                if p1 <= len(nums1)-1:
                    num1 = nums1[p1]
                if p2 <= len(nums2)-1:
                    num2 = nums2[p2]
                
                if num1 >= num2:
                    nums[i] = nums2[p2]
                    p2 += 1
                else:
                    nums[i] = nums1[p1]
                    p1 += 1
        
        return nums





            