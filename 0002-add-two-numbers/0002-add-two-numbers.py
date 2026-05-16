# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        quot = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + quot
            tail.next = ListNode(total % 10)
            quot = (val1 + val2 + quot) // 10

            tail = tail.next
       
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if quot > 0: tail.next = ListNode(quot)
        return dummy.next
