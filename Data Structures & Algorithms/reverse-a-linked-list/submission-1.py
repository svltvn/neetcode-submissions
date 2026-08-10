# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #elementary approach
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)

            curr = curr.next
        
        curr = None
        for i in range(len(arr)):
            prev = ListNode(arr[i])
            prev.next = curr
            curr = prev
        
        head = curr
        return head
            
            




