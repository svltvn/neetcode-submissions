# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        seen = set()
        curr = head

        while curr:
            if curr not in seen:
                seen.add(curr)
            else:
                return True
            
            curr = curr.next
        
        return False
        '''

        #2-pointer approach
        f, s  = head, head

        while f:
            f = f.next
            if f:
                f=f.next
            else: 
                return False
            s = s.next

            if f == s:
                return True
        
        return False

