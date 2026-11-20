# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        if list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1.next = self.mergeTwoLists(list1.next, list2)
            else:
                dummy.next = list2
                list2.next = self.mergeTwoLists(list1, list2.next)
        else:
            dummy.next = list1 or list2
        return dummy.next

        
    