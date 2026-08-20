class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use the previous problem of the sorted 2 sum before this
        nums = sorted(nums)

        #First iterate through nums
        ##Create subnums == num[i+1:]
        ###2pointer approach on subnums, where val == 0
        triplets = []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r:
                val = nums[l]+ nums[r] + nums[i]
                if val == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l+=1
                    r-=1
                elif val < 0:
                    l+=1
                else:
                    r-=1

        return triplets
        