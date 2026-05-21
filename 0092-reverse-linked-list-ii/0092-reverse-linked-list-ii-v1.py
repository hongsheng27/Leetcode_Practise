# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0, head)
        length = right - left
        while cur and left - 1:
            left -= 1
            cur = cur.next
        
        target = cur.next 
        cur.next = None
        prevLeft = cur
        cur = target

        while cur and length:
            length -= 1
            cur = cur.next
        end = None
        if cur:
            end = cur.next
            cur.next = None

        prevLeft.next = self.reverseList(target, end)
        return dummy.next

    def reverseList(self, node, end):
        prev = end
        cur = node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

        