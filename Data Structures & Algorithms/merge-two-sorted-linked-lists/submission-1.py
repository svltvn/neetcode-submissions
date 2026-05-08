# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l3head = l3
        if list1 == None and list2 == None:
            return None

        while list1 or list2:
            num1, num2 = 101,101
            if list1:
                num1 = list1.val
            if list2:
                num2 = list2.val
            
            if num1<=num2:
                print('1',num1, num2)
                l3.val = num1
                list1 = list1.next
                
            else:
                print('2',num1, num2)
                l3.val = num2
                list2 = list2.next
                
            if list1 or list2:
                l3.next = ListNode()
                l3 = l3.next
        return l3head
