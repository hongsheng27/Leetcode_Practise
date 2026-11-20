# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        def recursion(l1, l2, tail):
            if not l1 or not l2:
                tail.next = l1 or l2
                return
            
            if l1.val <= l2.val:
                tail.next = l1
                recursion(l1.next, l2, l1)
            else:
                tail.next = l2
                recursion(l1, l2.next, l2)  
        
        dummy = ListNode()
        recursion(list1, list2, dummy)
        return dummy.next