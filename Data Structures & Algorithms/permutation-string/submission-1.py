class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #iterate through s2
        ##when c in s2 in s1, open sliding window s2[i:len(s1)]
        ## check to see sorted(s[l:r]) == sorted(s2)

        for i in range(len(s2)): #need to be aware that i < len(s2)-len(s1)
            if s2[i] in s1:
                sort1 = sorted(s1)
                sort2 = sorted(s2[i:i+len(s1)])
                if sort1 == sort2:
                    return True
        
        return False


