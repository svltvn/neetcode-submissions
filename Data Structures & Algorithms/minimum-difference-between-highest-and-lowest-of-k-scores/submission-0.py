class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDif = nums[-1]-nums[0]
        for i in range(len(nums)-(k-1)):
            print(nums[i:i+k])
            dif = max(nums[i:i+k]) - min(nums[i:i+k])
            minDif = min(minDif, dif)
        return minDif
