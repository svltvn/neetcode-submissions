# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        i = 0
        l1 = head
        
        while l1:
            count +=1
            l1 = l1.next
        i = count-n
        if i == 0:
            return head.next
        
        count = 0
        l1 = head
        print(i)
        while l1:
            print(count)
            if count == i-1:
                l1.next = l1.next.next
            l1 = l1.next
            count += 1

        
        return head
