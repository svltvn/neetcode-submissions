# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #First Pass
        i = 0
        curr = head
        while curr:
            i+=1
            curr = curr.next
        print(i)


        #2nd pass
        if i == 1:
            return None
        
        j = i-n
        if j == 0:
            return head.next
        i=0
        curr = head
        while curr:
            i+=1
            print(i, curr.val)
            if i == j and curr.next:
                curr.next = curr.next.next
            curr = curr.next
        
        return head

        






        
