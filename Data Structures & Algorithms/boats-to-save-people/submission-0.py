class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people)-1
        boats = 0
        while l <= r:
            print(l, r)
            boats += 1
            if people[r] == limit:
                r-=1            
            elif people[r] < limit:
                if people[r]+people[l] <= limit:
                    l+=1
                r-=1
        
        return boats
