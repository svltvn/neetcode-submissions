class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2pointer approach
        #calculate maxArea based on minHeight
        #move smaller height over

        l, r = 0, len(heights)-1
        maxArea = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            length = r-l

            maxArea = max(maxArea, minHeight*length)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return maxArea