class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Idea for this will be to use a 2 pointer approach and then once a duplicate has been found
        #then go ahead and start sliding the window, once a bigger substring has been added than
        #update the 2 pointer approach

        maxLen = 0
        subStr = "" 

        for c in s:
            if c in subStr:
                l = subStr.find(c)+1
                subStr = subStr[l:]

            subStr += c
            maxLen = max(maxLen, len(subStr))
        
        return maxLen


        '''
        maxLen = 0
        start, stop = 0,0 
        for i in range(len(s)-1):
            if s[i] not in s[start:stop]:
                stop += 1
                print(s[start:stop])
                maxLen = max(maxLen, stop-start)
            else:
                start = s[start:stop].index(s[i])+1
                stop += 1
        
        return maxLen
        '''