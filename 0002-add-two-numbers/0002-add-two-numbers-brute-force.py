# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        place = 1
        num1 = 0
        while curr:
            num1 += int(curr.val) * place
            place *= 10
            curr = curr.next
        curr = l2
        place = 1
        num2 = 0
        while curr:
            num2 += int(curr.val) * place
            place *= 10
            curr = curr.next
        reverse_total = str(num1 + num2)[::-1]
        dummy = tail = ListNode()
        for n in reverse_total:
            tail.next = ListNode(int(n))
            tail = tail.next
        return dummy.next
            

        