class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        We can't do recursive, as the function doesn't return anything
        But there are only 3 possible values, so we actually need to sort 2 values
        Push all 0's to the begining of the list and 2's to the end, 1's will filter to the middle
        """
        i = 0
        l, r = 0, len(nums)-1
        while i <= r:
            print(i)
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
            elif nums[i] == 2:
                nums.append(nums.pop(i))
                i-=1
                r-=1
            i+=1
