class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        While trying to solve this, I tried sorting the problem, but after seeing the solution
        ordering does matter and we want to just use the window (subarrays), that are next in order
        '''

        res = []
        count = 0
        l, r = 0, k
        while r <= len(arr):
            subArr = arr[l:r]
            avg = sum(subArr)/k
            if avg >= threshold:
                count += 1
            
            l += 1
            r += 1
            
        return count


