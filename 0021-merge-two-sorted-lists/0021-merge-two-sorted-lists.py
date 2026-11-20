# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        def recursion(l1, l2, tail):
            dummy = tail
            if l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    tail = tail.next
                    recursion(l1.next, l2, tail)
                else:
                    tail.next = l2
                    tail = tail.next
                    recursion(l1, l2.next, tail)
            else:
                tail.next = l1 or l2
            return dummy
            
        
        dummy = ListNode()
        return recursion(list1, list2, dummy).next