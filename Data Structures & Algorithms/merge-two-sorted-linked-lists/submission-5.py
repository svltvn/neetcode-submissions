# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        
        while list2:
            arr.append(list2.val)
            list2 = list2.next
        
        arr.sort()
        print(arr)
        list3 = ListNode()
        returnHead = list3
        if not arr:
            return None
        
        for i in range(len(arr)):
            if i == 0:
                list3 = ListNode(arr[i])
                returnHead = list3
            else:
                list3.next=ListNode(arr[i])
                list3 = list3.next
            

        
        return returnHead


                
