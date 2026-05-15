# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l1 = []
        while head:
            if head.val != val:
                l1.append(head.val)
            head = head.next
        if not l1:
            return None
        returnList = ListNode()
        dummy = returnList
        for i in range(len(l1)):
            returnList.val = l1[i]
            if i < len(l1)-1:
                returnList.next = ListNode()
            returnList = returnList.next
        return dummy


        