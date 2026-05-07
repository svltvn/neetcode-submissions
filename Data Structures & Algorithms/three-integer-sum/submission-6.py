class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numLists=[]
        nums.sort()
        print(nums)

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]

                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    numList = [nums[i], nums[l], nums[r]]
                    numList.sort()
                    if numList not in numLists:
                        numLists.append(numList)
                    r-=1
                    l+=1


        return numLists